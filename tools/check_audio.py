#!/usr/bin/env python3
"""Transkribiert eine Folge mit Whisper, um falsch gesprochene Wörter zu finden.

Benutzung:
    pip install faster-whisper
    python3 tools/check_audio.py folgen/<folge>/<datei>.mp3 [modell] > transkript.txt

Ziffern im Transkript sind normal (Whisper schreibt Zahlen als Ziffern).
Gesucht werden verstümmelte Wörter, englisch gesprochene Wörter und Lücken.
"""
import subprocess
import sys

import numpy as np
from faster_whisper import WhisperModel

raw = subprocess.run(
    ["ffmpeg", "-loglevel", "error", "-i", sys.argv[1], "-f", "s16le", "-ac", "1", "-ar", "16000", "-"],
    capture_output=True, check=True).stdout
audio = np.frombuffer(raw, np.int16).astype(np.float32) / 32768.0
model = WhisperModel(sys.argv[2] if len(sys.argv) > 2 else "small", device="cpu", compute_type="int8")
segments, _ = model.transcribe(audio, language="de", beam_size=5)
for seg in segments:
    m, s = divmod(int(seg.start), 60)
    print(f"[{m:02d}:{s:02d}] {seg.text.strip()}", flush=True)
