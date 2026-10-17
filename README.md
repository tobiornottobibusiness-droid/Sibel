# Sicherheitsbeleuchtung verstehen – Referenzanlage INOTEC CPS 220/64

Eine Lernreihe zum Hören (z. B. beim Autofahren), mit Begleitheften zum Nachlesen. Sie erklärt Sicherheitsbeleuchtungsanlagen von Grund auf. Als Referenz dient eine konkrete Anlage, die **INOTEC CPS 220/64** (mit Blick auf die Nachfolgerin CPS FUSION), damit sich das Wissen später auf jede andere Anlage übertragen lässt.

**Zielgruppe:** Elektrofachkraft (Energie- und Gebäudetechnik). Wechselstrom-Grundlagen werden vorausgesetzt, Gleichstrom- und Batterietechnik werden gezielt aufgefrischt.

## Inhalt des Repos

| Ordner | Inhalt |
|--------|--------|
| [`wissensbasis/`](wissensbasis/) | Recherchiertes Fachwissen: [Anlage CPS 220/64](wissensbasis/04-cps-220-64.md), [Anlage CPS FUSION](wissensbasis/01-cps-fusion-anlage.md), [Normen & Regeln (Stand 10/2026)](wissensbasis/02-normen-und-regeln.md), [Glossar](wissensbasis/03-glossar.md), Praxisbeispiele [Gessler SiBELON](wissensbasis/05-praxisbeispiel-gessler-sibelon.md) und [Kaufel viaFlex](wissensbasis/06-praxisbeispiel-kaufel-viaflex.md), [Quellen](wissensbasis/quellen.md) |
| [`folgen/`](folgen/) | Je Folge: `…mp3` (Audio), `begleitheft.md` (Spickzettel, Selbsttest, Praxisauftrag), `skript.md` (wörtliches Skript), `kapitel.txt` (Kapitelmarken) |
| [`tools/`](tools/) | `make_episode.py`: erzeugt aus einem Skript die MP3 (zwei Stimmen, Denkpausen, Kapitel-Gong) |

## Staffelplan

| # | Folge | Kerninhalte | Status |
|---|-------|-------------|--------|
| 1 | **Das große Bild** | Wozu Sicherheitsbeleuchtung, Begriffsbaum, 1 lx/0,5 lx/15 lx, Umschaltzeit und Nennbetriebsdauer, Schaltungsarten, Netzausfall HV vs. UV, EB/LPS/CPS, **die 5 Bausteine** | ✅ fertig |
| 2 | **Gleichstrom für Wechselstrom-Profis** | Warum LED-Geräte DC vertragen, Batterie-Spannungen pro Zelle (≈ 245 V statt 216 V), Ah/Wh und Entladezeit, Überschlag, **die 6 Gleichstrom-Regeln** (Lichtbogen, Batterie, N im Notbetrieb, Freischalten, Körperwirkung, Polarität), I-T-Prinzip, Messen an DC, Schaltreihenfolge | ✅ fertig |
| 3 | **Recht und Normen kompakt** | Wer verlangt was (Baurecht, Arbeitsschutz, Sonderbauten), EN 1838:2025 (neu: 1 lx flächig), EN 50172:2024 + Übergang bis 27.05.2027, EN 50171, VDE 0100-560-1 (20 Leuchten/60 %, 2 Kreise je Brandabschnitt), MLAR/E30, Prüfpflichten, Verantwortung, Qualifikation | ✅ fertig |
| 4 | **Die Anlage lesen: CPS 220/64 von außen nach innen** | Typenschild entschlüsseln und prüfen, Typenbezeichnung, Schrankaufbau, Baugruppenträger, Klemmleisten X1/X2/X3 (+X4/X5/X8), Betriebsmittelkennzeichen (=, +, −; F, X, A, K, Q, G, T), Plan lesen, Methode „vom Verbraucher zur Quelle“; Praxisfall Kaufel-Unterstation; Transfer-Ecke: Gessler SiBELON und Kaufel viaFlex | ✅ fertig |
| 5 | **Die Batterie in der Praxis** | Bauarten (verschlossen OGi/Vlies/Gel vs. geschlossen OPzS), Alterung und 25 % Reserve, Temperatur (+10 °C ≈ halbe Lebensdauer), Tiefentladung und Sulfatierung, Einzelblocküberwachung (BCS), Inspektion und Protokoll, Batterietausch, Wasserstoff/Lüftung/Aufstellraum; Transfer: Gessler (verschlossen) und Kaufel (OPzS 1200 Ah) | ✅ fertig |
| 6 | **Netz, Laden, Umschalten** | Ladeteil und I-U-Kennlinie, Umschaltbetrieb, 12 h/80 %, Netzausfall HV (RIF 5, Meldekontakte, Umschaltzeiten) und UV (DPÜ, Stromschleife, Fail-safe, Zener-Abschluss, DPÜ/B.2), Nachlauf, Handrückschaltung, Blockieren/Fernschalter, **24-V-Hilfsversorgung**; Transfer: Gessler und Kaufel (BS(M), DS) | ✅ fertig |
| 7 | Stromkreise | CP 4x2A/2x4A/1x6A (FUSION: CF …), Sicherungen, LEDs, 20 Leuchten/60 %, Einschaltstrom, Joker-Mischbetrieb in der Praxis, Lichtschalterabfrage (LSA), Brandabschnitte, Isolationsmessung Schritt für Schritt | geplant |
| 8 | Leuchten und Betriebsgeräte | Rettungszeichen vs. Sicherheitsleuchte, Erkennungsweite und Montagehöhe, Joker-EVG/J-SV-Modul (Mikro- und Adressschalter), Überwachungsarten, Leuchtentausch und neu einlernen, LED-Fehlerbilder, dynamische Leuchten | geplant |
| 9 | Erweiterungen und Busse | IB1/IB2/IB3, RTG, Unterstation CPUS vs. BUS-Unterstation CPUSB, MTB, Leitungslängen, Funktionserhalt E30, was bei Busausfall passiert | geplant |
| 10 | Bedienung und Software | Display-Menü, Statusfarben, Prüfbuch lesen, Tests starten, richtig blockieren, Konfigurator, INOWeb/INOView, Gebäudeleittechnik | geplant |
| 11 | Prüfen und Warten in der Praxis | Ein kompletter Wartungsbesuch als Geschichte: Ankommen, Sichtprüfung, Prüfbuch, Funktions-/Betriebsdauertest, Batterie, Messungen, Dokumentation, Übergabe an den Betreiber; alle Intervalle | geplant |
| 12 | Fehlersuche mit System | Methode Symptom → Baustein → Messung; Fälle: Leuchtenstörung, Netzausfall UV ohne Grund, Isolationsfehler, Busstörung, Tiefentladung, 24-V-Netzteil defekt | geplant |
| 13 | Transfer und Abschluss | Jede Anlage in 10 Minuten verstehen: die 5 Bausteine bei INOTEC, Gessler SiBELON und anderen Herstellern; Abschlussquiz über die ganze Reihe | geplant |

Jede Folge ab Folge 3 hat zusätzlich eine kurze **Transfer-Ecke**: Wie sieht das bei anderen Herstellern aus (z. B. Gessler SiBELON)?

**Rhythmus:** eine Folge pro Abend (ca. 20 Uhr). Feedback und Fragen aus dem Chat landen in [`FEEDBACK.md`](FEEDBACK.md) und fließen in die jeweils nächste Folge ein.

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
- Tempo: `RATE = "+15%"` in `tools/make_episode.py` (ca. 1,2-fach gegenüber der ersten Fassung). Denkpausen bleiben unverändert lang.
- Ausgabe: MP3, Mono, 64 kbit/s, auf −16 LUFS normalisiert (gut für Autolautsprecher), mit Kapitelmarken.
- Schon erzeugte Sätze werden in `.tts-cache/` zwischengespeichert. Bei Änderungen werden nur die geänderten Zeilen neu erzeugt.
- Qualitätskontrolle: Jede Folge wird per Spracherkennung (Whisper) gegengehört. Bisherige Aussprache-Erkenntnisse für die mehrsprachigen Stimmen:
  - Kürzel mit Bindestrich buchstabieren lassen: „C-P-S“, „D-P-Ü“, „L-P-S“, „DIN E-N“, „U-V“.
  - „Perfekt“ wird englisch gesprochen. Besser „Klasse“ oder „Sehr gut“.
  - „Amperestunde“ → „Ampere-Stunde“ schreiben.
  - „Zweitens:“ am Satzanfang (Sabine) klingt verwaschen. Besser „Als Zweites:“.
  - „einhundertacht“ statt „hundertacht“ schreiben. Zahlen nicht als kurzes Satzfragment an den Satzanfang stellen.
  - Betriebsmittelkennzeichen Ziffer für Ziffer schreiben („F eins null eins“), „einhunderteins“ klingt wie „Heinz“. „Kaufel Via-Flex“ besser umschreiben („ein System von Kaufel“).

## Wichtiger Hinweis

Das ist Lernmaterial. Es ersetzt weder die Herstellerunterlagen noch eine Einweisung oder den Normtext. Bei der Arbeit an Anlagen gelten die Sicherheitsregeln (216 V DC Batteriespannung, 5 Sicherheitsregeln, Freigabe durch die verantwortliche Elektrofachkraft).
