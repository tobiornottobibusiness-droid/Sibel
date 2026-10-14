# Arbeitsanweisung: Lernreihe Sicherheitsbeleuchtung

Dieses Repo enthält eine Audio-Lernreihe (Deutsch) über Sicherheitsbeleuchtung mit der **INOTEC CPS 220/64** als Referenzanlage (Nachfolgerin CPS FUSION als Seitenblick). Staffelplan und Status stehen in `README.md`.

## Hörer-Profil
- Elektrofachkraft mit Ausbildung Energie- und Gebäudetechnik, in der Probezeit bei einem Betrieb für Sicherheitsbeleuchtung.
- Wechselstrom-Grundlagen sitzen. Gleichstrom- und Batterietechnik werden gezielt aufgefrischt. Beim Thema Sicherheit spezifisch und konkret werden.
- Hört beim Autofahren. Mag den Aufbau, die Stimmen und das Tempo `+15%`.

## Abendlicher Ablauf (eine Folge pro Abend)
1. In `README.md` die erste Folge mit Status „geplant“ suchen. **Nur diese eine Folge** produzieren.
2. Fakten aus `wissensbasis/` nehmen. Nur bei Lücken gezielt recherchieren (Primärquellen: INOTEC-Handbücher, siehe `wissensbasis/quellen.md`). Neue Fakten mit Quelle in die Wissensbasis eintragen. Nichts erfinden. Wenn Quellen sich widersprechen, das sagen.
3. `folgen/folge-NN-<kurzname>/skript.md` schreiben, im Stil der vorherigen Folgen:
   - Dialog SABINE (Expertin) / TIM (Elektrofachkraft, Einsteiger in der Sicherheitsbeleuchtung), ca. 3.300–3.800 Wörter (≈ 25–28 min).
   - Kapitel (`## …`): Rückblick mit 3 Abruffragen zur Vorfolge und `[PAUSE 6–8]` → Inhalt in 4–7 Kapiteln → „Wiederholung mit Denkpausen“ (6–7 Fragen) → „Praxisauftrag und Ausblick“.
   - Analogien, „Warum?“-Fragen von Tim, Tim fasst in eigenen Worten zusammen, Sicherheitshinweise konkret.
   - **Alle Zahlen ausschreiben.** Keine Ziffern, kein %, °, /, lx, kW, Ah, mm im Sprechtext.
   - Aussprache: Kürzel mit Bindestrich („C-P-S“, „D-P-Ü“, „B-C-S“, „P-E“, „I-T-System“). Nicht „Perfekt“ (wird englisch gesprochen), sondern „Klasse“ / „Sehr gut“. „Ampere-Stunde“ mit Bindestrich. Bei Sabine nicht „Zweitens:“ am Satzanfang, sondern „Als Zweites:“. „einhundertacht“ statt „hundertacht“. Zahlen nicht als kurzes Satzfragment an den Satzanfang stellen (vor allem bei Tim), sondern in ganze Sätze einbetten.
4. `begleitheft.md` schreiben: Lernziele, Spickzettel mit Ziffern/Tabellen, Selbsttest mit aufklappbaren Antworten, Praxisauftrag.
5. Audio erzeugen: `pip install -r tools/requirements.txt` (falls nötig), dann `python3 tools/make_episode.py --check …/skript.md` und `python3 tools/make_episode.py …/skript.md`.
6. Gegenhören: Mit Whisper (`pip install faster-whisper`, Modell `small`, Audio per ffmpeg als 16-kHz-Array übergeben) transkribieren und auf falsch gesprochene Wörter prüfen. Betroffene Zeilen umformulieren und neu erzeugen (der Cache macht das schnell).
7. In `README.md` den Status auf „✅ fertig“ setzen. Committen und auf `claude/sicherheitsbeleuchtung-grundlagen-p0h5d1` pushen.
8. MP3 und Begleitheft per SendUserFile an den Nutzer schicken. Kurze Nachricht dazu: Thema, Länge, Kernpunkte.
9. Sind alle Folgen des Staffelplans fertig, die abendliche Routine deaktivieren und dem Nutzer Bescheid geben.

## Sicherheit
Inhalte sind Lernmaterial. Bei Arbeitsanweisungen immer auf die Betriebsanweisung des Betriebs und die Herstelleranleitung verweisen. Keine Abkürzungen bei Sicherheitsregeln (216 V DC, Batterie nicht abschaltbar, Freischalten an der Anlage, allpolig prüfen).
