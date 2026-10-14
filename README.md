# Sicherheitsbeleuchtung verstehen – Referenzanlage INOTEC CPS FUSION

Eine Lernreihe zum Hören (z. B. beim Autofahren), mit Begleitheften zum Nachlesen. Sie erklärt Sicherheitsbeleuchtungsanlagen von Grund auf. Als Referenz dient eine konkrete Anlage, damit sich das Wissen später auf jede andere Anlage übertragen lässt.

## Inhalt des Repos

| Ordner | Inhalt |
|--------|--------|
| [`wissensbasis/`](wissensbasis/) | Recherchiertes Fachwissen: [Anlage CPS FUSION](wissensbasis/01-cps-fusion-anlage.md), [Normen & Regeln (Stand 10/2026)](wissensbasis/02-normen-und-regeln.md), [Glossar](wissensbasis/03-glossar.md), [Quellen](wissensbasis/quellen.md) |
| [`folgen/`](folgen/) | Je Folge: `…mp3` (Audio), `begleitheft.md` (Spickzettel, Selbsttest, Praxisauftrag), `skript.md` (wörtliches Skript), `kapitel.txt` (Kapitelmarken) |
| [`tools/`](tools/) | `make_episode.py`: erzeugt aus einem Skript die MP3 (zwei Stimmen, Denkpausen, Kapitel-Gong) |

## Staffelplan

| # | Folge | Kerninhalte | Status |
|---|-------|-------------|--------|
| 1 | **Das große Bild** | Wozu Sicherheitsbeleuchtung, Begriffsbaum, 1 lx/0,5 lx/15 lx, Umschaltzeit und Nennbetriebsdauer, Schaltungsarten, Netzausfall HV vs. UV, EB/LPS/CPS, **die 5 Bausteine** | ✅ fertig |
| 2 | Elektro-Grundlagen für die Anlage | Spannung, Strom, Leistung, AC/DC, Amperestunden und Wattstunden, Ladespannung (warum ≈ 240 V statt 216 V), Rechenbeispiel Batteriedimensionierung | geplant |
| 3 | Recht und Normen kompakt | Baurecht, Arbeitsschutz, EN 1838:2025, EN 50172:2024 + Übergang, EN 50171, VDE 0100-560, MLAR/E30, Prüfpflichten | geplant |
| 4 | Die CPS FUSION von außen nach innen | Typen 1,5–22 kW, Typenschild, Schrankaufbau, Steuerteil, Baugruppenträger, Klemmleisten X1/X2/X3 | geplant |
| 5 | Baustein 3: Die Batterie | OGi-Blöcke, 216 V, Alterung und 25 % Reserve, Temperatur, Tiefentladeschutz 185 V, Lüftung, BCS | geplant |
| 6 | Bausteine 1+2: Netz, Ladeteil, Umschaltung | Ladeteile, 12 h/80 %, RIF 5, DPÜ/Stromschleife, Nachlauf, Handrückschaltung, Blockieren | geplant |
| 7 | Baustein 4: Stromkreismodule und Endstromkreise | CF 4x1A/2x2,5A/1x5A, Sicherungen, LEDs, 20 Leuchten/60 %, Mischbetrieb, 24-V-Technik | geplant |
| 8 | Leuchten und Betriebsgeräte | Rettungszeichen vs. Sicherheitsleuchte, FLD/FMD, Einzel-LED-Überwachung, Learn-Mode, Stromkreisprüfung, dynamische Leuchten | geplant |
| 9 | Erweiterungen und Busse | IB1/IB2/IB3, RTG, Unterstation CPUS vs. BUS-Unterstation CPUSB, LSA, MTB, Leitungslängen, Funktionserhalt | geplant |
| 10 | Bedienung und Software | Display, Statusfarben, Menü, Prüfbuch, Konfigurator, INOWeb, INOView, Gebäudeleittechnik | geplant |
| 11 | Prüfen und Warten in der Praxis | täglich bis 3-jährlich, Funktions- und Betriebsdauertest, Isolationsmessung, Batterieinspektion, Ein-/Ausschaltreihenfolge | geplant |
| 12 | Fehlersuche mit System | typische Meldungen, Denkweise, Fallbeispiele | geplant |
| 13 | Transfer | jede Anlage in 10 Minuten verstehen, die 5 Bausteine bei anderen Herstellern, Abschlussquiz | geplant |

## Wie die Reihe aufgebaut ist (Didaktik)

Die Folgen sind so gebaut, dass sie auch ohne Bildschirm funktionieren, also beim Autofahren:

1. **Ein Bezugsrahmen statt Faktensammlung.** Folge 1 legt eine „Landkarte“ an: die **5 Bausteine** jeder Zentralbatterieanlage. Jede weitere Folge zoomt in einen Baustein hinein. Neues Wissen hat so immer einen Platz, an dem es andocken kann.
2. **Dialog mit Fragen.** Eine Expertin erklärt, ein Einsteiger stellt die Fragen, die man selbst hätte („Warum?“, „Was passiert, wenn …?“). Zuhören bei einem Dialog mit solchen Fragen hilft beim Verstehen nachweislich mehr als ein Monolog (Craig et al., 2006, „vicarious learning“).
3. **Aktives Erinnern mit Denkpausen.** Am Ende jeder Folge kommen Fragen mit 6–10 Sekunden Stille. Selbst abrufen festigt Wissen stärker als erneutes Hören (Testing-Effekt, Roediger & Karpicke, 2006).
4. **Verteilte Wiederholung.** Jede Folge beginnt mit Fragen zur vorherigen. Eine Folge nach ein paar Tagen erneut zu hören ist ausdrücklich gewollt.
5. **Bilder statt Folien.** Analogien aus dem Auto (Ladeteil = Lichtmaschine, Prüfbuch = Scheckheft, Funktionstest = Lampentest beim Zündung-An) und Größenvergleiche (1 lx ≈ 4× Vollmond).
6. **Hören + Lesen + Anfassen.** Zu jeder Folge gibt es ein Begleitheft mit allen Zahlen und einen **Praxisauftrag** für die nächste Gelegenheit an einer echten Anlage. Theorie wird so mit dem verknüpft, was man im Keller wirklich sieht.
7. **Zahlen sicher aussprechen.** Alle Zahlen sind im Skript **ausgeschrieben** („zweihundertsechzehn Volt“, „DIN E-N fünfzig eins einundsiebzig“). Das Tool lehnt Skripte mit Ziffern ab. Dadurch ist die Aussprache unabhängig vom Sprachmodell korrekt.

**Empfohlener Rhythmus:** 1–2 Folgen pro Woche. Jede Folge zweimal hören (einmal direkt, einmal nach 3–5 Tagen). Begleitheft am Wochenende 10 Minuten durchsehen. Praxisauftrag beim nächsten Einsatz erledigen.

## Audio erzeugen

```bash
pip install -r tools/requirements.txt     # edge-tts; ffmpeg muss installiert sein
python3 tools/make_episode.py --check folgen/folge-01-das-grosse-bild/skript.md   # nur prüfen
python3 tools/make_episode.py folgen/folge-01-das-grosse-bild/skript.md           # MP3 erzeugen
```

- Stimmen: Microsoft-Neural-Stimmen über `edge-tts`. Sabine = `de-DE-SeraphinaMultilingualNeural`, Tim = `de-DE-FlorianMultilingualNeural`.
- Ausgabe: MP3, Mono, 64 kbit/s, auf −16 LUFS normalisiert (gut für Autolautsprecher), mit Kapitelmarken.
- Schon erzeugte Sätze werden in `.tts-cache/` zwischengespeichert. Bei Änderungen werden nur die geänderten Zeilen neu erzeugt.
- Qualitätskontrolle: Jede Folge wird per Spracherkennung (Whisper) gegengehört. Bisherige Aussprache-Erkenntnisse für die mehrsprachigen Stimmen:
  - Kürzel mit Bindestrich buchstabieren lassen: „C-P-S“, „D-P-Ü“, „L-P-S“, „DIN E-N“, „U-V“.
  - „Perfekt“ wird englisch gesprochen. Besser „Klasse“ oder „Sehr gut“.
  - „Amperestunde“ → „Ampere-Stunde“ schreiben.
  - „Zweitens:“ am Satzanfang (Sabine) klingt verwaschen. Besser „Als Zweites:“.

## Wichtiger Hinweis

Das ist Lernmaterial. Es ersetzt weder die Herstellerunterlagen noch eine Einweisung oder den Normtext. Bei der Arbeit an Anlagen gelten die Sicherheitsregeln (216 V DC Batteriespannung, 5 Sicherheitsregeln, Freigabe durch die verantwortliche Elektrofachkraft).
