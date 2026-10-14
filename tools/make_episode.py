#!/usr/bin/env python3
"""Erzeugt aus einem Folgen-Skript (Markdown) eine MP3-Datei mit zwei Stimmen.

Skriptformat (folgen/<folge>/skript.md):

    ---
    titel: Folge 1 – Das große Bild
    datei: folge-01-das-grosse-bild
    ---
    # Überschrift (wird nicht gesprochen)
    > Kommentar (wird nicht gesprochen)
    ## Kapitelname            -> Gong + Kapitelmarke in der MP3
    SABINE: Gesprochener Text.
    TIM: Gesprochener Text.
    [PAUSE 5]                 -> 5 Sekunden Stille (Denkpause)
    [GONG]                    -> Gong ohne Kapitelmarke

Zahlen müssen im Skript ausgeschrieben sein ("zweihundertsechzehn Volt").
Das Tool bricht ab, wenn es Ziffern findet. So ist die Aussprache unabhängig
vom TTS-Modell immer korrekt.

Benutzung:
    python3 tools/make_episode.py folgen/folge-01-das-grosse-bild/skript.md
"""

import argparse
import asyncio
import hashlib
import os
import re
import ssl
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

import edge_tts
import edge_tts.communicate as _communicate

# edge-tts bringt ein eigenes CA-Bundle mit (certifi). Hinter einem Proxy mit
# eigener CA wird stattdessen das System-Bundle aus SSL_CERT_FILE verwendet.
_cafile = os.environ.get("SSL_CERT_FILE") or os.environ.get("REQUESTS_CA_BUNDLE")
if _cafile and Path(_cafile).is_file():
    _communicate._SSL_CTX = ssl.create_default_context(cafile=_cafile)

VOICES = {
    "SABINE": "de-DE-SeraphinaMultilingualNeural",
    "TIM": "de-DE-FlorianMultilingualNeural",
}
RATE = "+15%"   # entspricht ca. 1,2-fachem Tempo gegenüber der ersten Fassung (-4 %)
SAMPLE_RATE = 24000
GAP_SAME_SPEAKER = 0.25
GAP_SPEAKER_CHANGE = 0.38
GAP_AROUND_GONG = 0.6

REPO = Path(__file__).resolve().parent.parent
CACHE_DIR = REPO / ".tts-cache"

LINE_SPEECH = re.compile(r"^([A-ZÄÖÜ]+):\s*(.+)$")
LINE_PAUSE = re.compile(r"^\[PAUSE\s+(\d+(?:[.,]\d+)?)\]$")


def parse_script(path):
    """Liest das Skript und gibt (metadaten, ereignisse) zurück."""
    text = path.read_text(encoding="utf-8")
    meta = {}
    if text.startswith("---"):
        _, front, text = text.split("---", 2)
        for line in front.strip().splitlines():
            key, _, value = line.partition(":")
            meta[key.strip()] = value.strip()

    events = []
    for lineno, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith(">") or re.match(r"^#(?!#)", line):
            continue
        if line.startswith("## "):
            events.append(("chapter", line[3:].strip(), lineno))
            continue
        if line == "[GONG]":
            events.append(("gong", None, lineno))
            continue
        m = LINE_PAUSE.match(line)
        if m:
            events.append(("pause", float(m.group(1).replace(",", ".")), lineno))
            continue
        m = LINE_SPEECH.match(line)
        if m:
            speaker, spoken = m.group(1), clean_text(m.group(2))
            if speaker not in VOICES:
                sys.exit(f"Zeile {lineno}: unbekannter Sprecher {speaker!r}")
            events.append(("speech", (speaker, spoken), lineno))
            continue
        sys.exit(f"Zeile {lineno}: Format nicht erkannt: {raw!r}")
    return meta, events


def clean_text(text):
    text = re.sub(r"[*_`]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def check_spoken_text(events):
    """Ziffern und Kürzel, die TTS-Modelle oft falsch lesen, ablehnen."""
    problems = []
    risky = re.compile(r"\d|%|°|\blx\b|\bkW\b|\bAh\b|\bmm\b|/")
    for kind, payload, lineno in events:
        if kind == "speech" and risky.search(payload[1]):
            problems.append(f"  Zeile {lineno}: {payload[1][:90]}")
    if problems:
        sys.exit("Ziffern/Kürzel im Sprechtext gefunden (bitte ausschreiben):\n"
                 + "\n".join(problems))


def cache_path(voice, text):
    digest = hashlib.sha1(f"{voice}|{RATE}|{text}".encode()).hexdigest()[:16]
    return CACHE_DIR / f"{digest}.wav"


async def synthesize(voice, text, target, semaphore):
    async with semaphore:
        for attempt in range(4):
            try:
                with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
                    tmp_mp3 = tmp.name
                await edge_tts.Communicate(text, voice, rate=RATE).save(tmp_mp3)
                subprocess.run(
                    ["ffmpeg", "-loglevel", "error", "-y", "-i", tmp_mp3,
                     "-ac", "1", "-ar", str(SAMPLE_RATE), "-sample_fmt", "s16", str(target)],
                    check=True)
                os.unlink(tmp_mp3)
                return
            except Exception as exc:  # Netzwerkfehler: kurz warten, erneut versuchen
                if attempt == 3:
                    raise
                print(f"  Wiederhole ({exc.__class__.__name__}) …", file=sys.stderr)
                await asyncio.sleep(2 ** (attempt + 1))


async def synthesize_all(events):
    CACHE_DIR.mkdir(exist_ok=True)
    semaphore = asyncio.Semaphore(4)
    jobs = []
    for kind, payload, _ in events:
        if kind == "speech":
            voice = VOICES[payload[0]]
            target = cache_path(voice, payload[1])
            if not target.exists():
                jobs.append(synthesize(voice, payload[1], target, semaphore))
    print(f"{len(jobs)} neue Sprachsegmente werden erzeugt …")
    await asyncio.gather(*jobs)


def make_gong(target):
    """Weicher Zweiklang-Gong als Kapiteltrenner."""
    expr = ("0.30*sin(2*PI*659*t)*exp(-5*t)"
            "+0.30*if(gte(t,0.4),sin(2*PI*523*(t-0.4))*exp(-4*(t-0.4)),0)")
    subprocess.run(
        ["ffmpeg", "-loglevel", "error", "-y", "-f", "lavfi",
         "-i", f"aevalsrc='{expr}':s={SAMPLE_RATE}:d=1.8",
         "-ac", "1", "-sample_fmt", "s16", str(target)],
        check=True)


def read_frames(path):
    with wave.open(str(path), "rb") as w:
        return w.readframes(w.getnframes())


def silence(seconds):
    return b"\x00\x00" * int(SAMPLE_RATE * seconds)


def assemble(events, out_wav):
    """Fügt alle Segmente zusammen und gibt Kapitel-Startzeiten (s) zurück."""
    gong_path = CACHE_DIR / "gong.wav"
    if not gong_path.exists():
        make_gong(gong_path)
    gong = read_frames(gong_path)

    chunks, chapters, position = [], [], 0.0
    last_speaker = None

    def add(data):
        nonlocal position
        chunks.append(data)
        position += len(data) / 2 / SAMPLE_RATE

    add(silence(0.5))
    for kind, payload, _ in events:
        if kind in ("chapter", "gong"):
            if kind == "chapter":
                chapters.append((position, payload))
            add(silence(GAP_AROUND_GONG))
            add(gong)
            add(silence(GAP_AROUND_GONG))
            last_speaker = None
        elif kind == "pause":
            add(silence(payload))
            last_speaker = None
        else:
            speaker, text = payload
            if last_speaker is not None:
                add(silence(GAP_SAME_SPEAKER if speaker == last_speaker else GAP_SPEAKER_CHANGE))
            add(read_frames(cache_path(VOICES[speaker], text)))
            last_speaker = speaker
    add(silence(1.0))

    with wave.open(str(out_wav), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SAMPLE_RATE)
        w.writeframes(b"".join(chunks))
    return chapters, position


def write_ffmetadata(path, meta, chapters, total):
    lines = [";FFMETADATA1",
             f"title={meta.get('titel', 'Folge')}",
             "artist=Lernreihe Sicherheitsbeleuchtung",
             "album=Sicherheitsbeleuchtung verstehen – Referenzanlage INOTEC CPS FUSION",
             "genre=Podcast"]
    for i, (start, title) in enumerate(chapters):
        end = chapters[i + 1][0] if i + 1 < len(chapters) else total
        lines += ["[CHAPTER]", "TIMEBASE=1/1000",
                  f"START={int(start * 1000)}", f"END={int(end * 1000)}", f"title={title}"]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def fmt_time(seconds):
    m, s = divmod(int(round(seconds)), 60)
    return f"{m:02d}:{s:02d}"


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("skript", type=Path)
    parser.add_argument("--check", action="store_true", help="nur Skript prüfen, kein Audio")
    args = parser.parse_args()

    meta, events = parse_script(args.skript)
    check_spoken_text(events)
    n_speech = sum(1 for e in events if e[0] == "speech")
    n_words = sum(len(e[1][1].split()) for e in events if e[0] == "speech")
    print(f"{n_speech} Sprechzeilen, {n_words} Wörter (≈ {n_words / 135:.0f} min)")
    if args.check:
        return

    asyncio.run(synthesize_all(events))
    out_dir = args.skript.parent
    stem = meta.get("datei", args.skript.parent.name)
    with tempfile.TemporaryDirectory() as tmp:
        raw_wav = Path(tmp) / "roh.wav"
        chapters, total = assemble(events, raw_wav)
        ffmeta = Path(tmp) / "meta.txt"
        write_ffmetadata(ffmeta, meta, chapters, total)
        out_mp3 = out_dir / f"{stem}.mp3"
        subprocess.run(
            ["ffmpeg", "-loglevel", "error", "-y", "-i", str(raw_wav), "-i", str(ffmeta),
             "-map_metadata", "1", "-map_chapters", "1",
             "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
             "-ar", str(SAMPLE_RATE), "-ac", "1", "-c:a", "libmp3lame", "-b:a", "64k",
             "-id3v2_version", "3", str(out_mp3)],
            check=True)

    kapitel = out_dir / "kapitel.txt"
    kapitel.write_text("".join(f"{fmt_time(t)}  {name}\n" for t, name in chapters),
                       encoding="utf-8")
    print(f"Fertig: {out_mp3} ({fmt_time(total)} min)")
    print(kapitel.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
