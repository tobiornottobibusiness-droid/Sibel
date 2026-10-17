# Begleitheft Folge 6 – Netz, Laden, Umschalten

**Audio:** [folge-06-netz-laden-umschalten.mp3](folge-06-netz-laden-umschalten.mp3) · **Kapitelmarken:** [kapitel.txt](kapitel.txt) · **Wörtliches Skript:** [skript.md](skript.md)
**Ausführlich:** [wissensbasis/01-cps-fusion-anlage.md](../../wissensbasis/01-cps-fusion-anlage.md) (Abschnitt 4 und 5), [wissensbasis/04-cps-220-64.md](../../wissensbasis/04-cps-220-64.md) (Abschnitt 9) · Lernmaterial, ersetzt weder Herstelleranleitung noch Betriebsanweisung

## Lernziele
Nach dieser Folge kannst du …
1. erklären, wie ein Ladeteil nach I-U-Kennlinie lädt, und weißt, was „12 h / 80 %“ bedeutet.
2. Netzausfall am Hauptverteiler und Netzausfall in einer Unterverteilung unterscheiden, mit Erkennung und Reaktion.
3. die 24-V-Stromschleife und das Fail-safe-Prinzip erklären.
4. Nachlauf, Handrückschaltung, Blockieren und Fernschalter richtig einordnen.
5. sagen, wozu die 24-V-Netzteile da sind, und typische Fehler erkennen.

## Spickzettel

### Ladeteil („Lichtmaschine“)
| Thema | Inhalt |
|---|---|
| INOTEC-Ladeteile | 1,2 A / 3 A / 7 A; je Ladeteil eigene AC- und DC-Sicherung + Schalter; mehrere je Anlage möglich |
| I-U-Kennlinie | **I-Phase:** Strom begrenzt → **U-Phase:** Spannung konstant, Strom sinkt von allein („Zapfpistole schaltet kurz vor voll auf langsam“) |
| Stufen | Starkladung bis 2,4 V/Zelle → Erhaltungsladung ≈ 2,3 V/Zelle; Umschaltpunkt je nach Batteriehersteller |
| Umschaltbetrieb | Im Netzbetrieb hängen die Leuchten **am Netz** (AC über die Anlage), die Batterie wird nur geladen |
| EN 50171 | nach **12 h** Laden wieder **80 %** der Nennbetriebsdauer; Alterungsreserve zählt dabei nicht |
| Netzseite | LT 7 A zieht ≈ 9 A (≈ 2.100 VA): 7 A × ≈ 250 V ≈ 1.750 W, geteilt durch 230 V, plus Verluste |
| Temperatur | Fühler im Batterieraum (RIF 5 T+/T−) oder BCS → temperaturgeführte Ladespannung; Lüfter über RIF-5-Kontakt bei Starkladung |
| Ladestrom am Display | klein = Erhaltungsladung; groß = Nachladen nach Test; tagelang groß ohne Test → genauer hinsehen |
| Ladeteil gestört | sofort beheben: nach der nächsten Entladung droht Tiefentladung |

### Zwei Arten Netzausfall
| | Netzausfall **Hauptverteiler** (HV) | Netzausfall **Unterverteilung** (UV) |
|---|---|---|
| Wo | Einspeisung der Anlage selbst | Unterverteilung der Allgemeinbeleuchtung |
| Erkannt durch | **RIF 5** (ab Werk verdrahtet), bei 3~ integrierte DPÜ | **DPÜ** an der 24-V-Stromschleife oder **DPÜ/B.2** am Bus |
| Reaktion | **Batteriebetrieb**: alle Leuchten auf 216 V DC | angeschlossene Leuchten in **Dauerlicht** |
| Strom kommt aus | **Batterie** | **Netz** über die Anlage (Batterie wird geschont) |
| Display | Batteriebetrieb | „Netzausfall UV“ |

**Umschaltzeit:** bisherige Vornorm 1 s (Versammlungs-, Verkaufsstätten), sonst oft 15 s · EN: 50 % nach 5 s, 100 % nach 60 s, empfohlen ≤ 2 s · ASR A2.3: 1 s bei vielen ortsunkundigen Personen · im Einzelfall Brandschutzkonzept.

**RIF-5-Meldekontakte** (Betrieb / Störung / Batteriebetrieb):
| Kontakt | Betrieb | Störung | Batteriebetrieb |
|---|---|---|---|
| 1–2 „Störung“ | geschlossen | **offen** | geschlossen |
| 3–4 „Betrieb“ | geschlossen | offen | offen |
| 5–6 „Batteriebetrieb“ | offen | offen | geschlossen |
| 7–8, 9–10 | Option 1/2, frei programmierbar | | |

Meldetableau (MTB): grün Betrieb, gelb Batteriebetrieb, rot Störung, Schlüsselschalter zum Blockieren → tägliche Sichtkontrolle an ständig besetzter Stelle.

### DPÜ und Stromschleife
- DPÜ in der UV der Allgemeinbeleuchtung: Ansprechwert **0,85 · U<sub>N</sub>**, LED je Phase, auch einphasig, 1 Wechsler.
- Schleife **SL+/SL−** am RIF 5, alle DPÜ-Kontakte **in Reihe**, ab Werk Drahtbrücke (beim Anschluss entfernen).
- **Fail-safe:** Kontakt **öffnet** bei Ausfall. Jede Unterbrechung (Phase weg, Draht ab, DPÜ defekt) → Licht **EIN** („Menschenkette, einer lässt los“).
- **Zener-Abschlussklemme** am letzten DPÜ → auch **Kurzschluss** der Schleife wird erkannt.
- Länge: 500 m bei 0,5 mm², 2.000 m bei 1,5 mm². Für mehrere Stränge: Modul zur Einzelstrang-Überwachung (LOMO).
- **DPÜ/B.2** (Bus IB2 oder IB3, kein Mischbetrieb): meldet Standort + Phase (Menü Komponenten, rote LED), **Versorgung über den Bus**; Bus unterbrochen → „Kommunikationsstörung“ + Notlicht EIN.
- Auch DALI/KNX der Allgemeinbeleuchtung überwachen: Bus aus → Sicherheitsbeleuchtung EIN.
- ⚠️ UV der Allgemeinbeleuchtung abschalten = Notlicht geht **an**. Freischalten an der Anlage selbst.

### Zurückschalten
| Funktion | Bedeutung | Wo |
|---|---|---|
| **Nachlauf** | Notlicht bleibt nach Netzwiederkehr an, bis die Allgemeinbeleuchtung voll hell ist; DPÜ/B.2: 0/5/10/15 min, LEDs blinken währenddessen | Errichtungsnorm VDE V 0100-560-1 |
| **Handrückschaltung** | in betriebsmäßig verdunkelten Räumen (Kino, Theater) erst nach manueller Bestätigung zurück | Menü Funktionen → „Handrückschaltung quittieren“ (Display gelb); vorher prüfen, ob im Raum Licht ist |

### Blockieren und Fernschalter
- Blockieren: **Dauerlicht** oder **Dauer- und Notlicht** (Menü Funktionen, Status „Gerät blockiert“).
- Zweck: außerhalb der Nutzungszeit Tiefentladung bei langem Netzausfall vermeiden.
- ⚠️ „Dauer- und Notlicht blockiert“ vergessen = **kein Notlicht** bei Netzausfall.
- Fernschalter **FS+/FS−** am RIF 5 (externer Schalter, z. B. MTB-Schlüsselschalter). Freigabe nur dort, wo blockiert wurde.
- **Blockieren ≠ Freischalten.** Ausschaltreihenfolge: **blockieren → Batteriesicherungen ziehen → Netz aus.** Nie unter Last schalten. Freischalten nach den 5 Sicherheitsregeln, allpolig prüfen.

### 24-V-Hilfsversorgung (deine Frage)
| Punkt | Inhalt |
|---|---|
| Wann laufen sie? | **immer**, sie „springen nicht an“ |
| Wozu? | 24 V DC für Steuerung, E/A-Module, Relais, Überwachungsschleifen, Meldekontakte, Busse = **das Gehirn** |
| Warum 24 V? | Elektronik ist für Kleinspannung gebaut; lange Schleifen und Busse sind mit Kleinspannung einfacher und sicherer |
| Bei Netzausfall | Mean Well DR-60 verträgt **124–370 V DC** → kann direkt aus der Batterie (≈ 190–260 V) laufen; ob so verdrahtet, zeigt der Schaltplan |
| INOTEC | Anlage liefert +24 V und ⊥ an **X2** für Busse und Stromschleife; Grund-Set mit eigenem 24-V-Netzteil für die erste LSA; Repeater ohne 24 V → Busstörung; Busausfall → CPUSB und DPÜ/B schalten Licht EIN |

**Typische Fehler:**
| Fehler | Woran du es merkst |
|---|---|
| Netzteil defekt / Vorsicherung ausgelöst | LED **„DC OK“ aus**, keine 24 V an +V/−V; Geräte-, Bus- oder Systemstörung; viele Anlagen schalten alle Leuchten ein |
| Kurzschluss / Überlast auf der 24-V-Seite (z. B. Leitung zum Tableau) | Netzteil schaltet ab oder taktet, Steuerung startet immer wieder neu |
| Alterung (Kondensatoren) | zu niedrige oder schwankende 24 V, sporadische Störungen |

**Schnellcheck:** LED „DC OK“ → Ausgang +V/−V im **DC-Bereich** messen (≈ 24 V). ⚠️ Eingangsseite: 230 V AC und ggf. Batteriespannung. Vertiefung in Folge 12.

### Transfer-Ecke
| | Gessler SiBELON | Kaufel viaFlex |
|---|---|---|
| Netzüberwachung HV | Dreiphasenrelais K'Electric: 85 % U<sub>N</sub>, 0,5 s, 2 Wechsler, Testtaster | Netz an der Zentrale (-F101 … -F103) |
| Netzüberwachung UV | – | Relais „Spannungsüberwachung -K03 … -K011“ in der Etagenverteilung → Eingänge „Netzüberwachung 1–4“ der Unterstation (Leitung überwacht), Modul viaFlex NÜV im Unterverteiler |
| Laden | Sicherungen „Ladung DC“; Display: 1,10 A (für 18 Ah eher viel → nach einigen Stunden erneut ablesen) | Ladeteil 220 V / **75 A** |
| Handrückschaltung | – | **BS(M) quittieren** = Bereitschaftsschaltung manuell (passt zum Theater) |
| Dauerlicht | – | **DS(Netz)** je Unterstation zentral aktivieren/blockieren |
| 24 V | 2 × Mean Well DR-60-24 | ABB CP-D 24/0.42 im Unterverteiler |

**Frage für deinen nächsten Schrank:** Wo sitzen Netzüberwachung und 24-V-Netzteil? Woran erkennst du sie, woher kommen ihre Leitungen, leuchtet „DC OK“?

## Selbsttest
1. Was bedeutet die I-U-Kennlinie?
2. Wie schnell muss eine entladene Batterie wieder geladen sein?
3. Netzausfall HV gegen Netzausfall UV: Reaktion und Stromquelle?
4. Warum öffnet der DPÜ-Kontakt bei Netzausfall?
5. Wozu dient die Handrückschaltung?
6. Reihenfolge beim Ausschalten der Anlage?
7. Wann laufen die 24-V-Netzteile, und was prüfst du zuerst?
8. *(Bonus)* Warum zieht ein 7-A-Ladeteil rund 9 A aus dem Netz?

<details><summary>Antworten</summary>

1. Erst Strom begrenzen (I), dann bei Erreichen der Ladespannung Spannung konstant halten (U), der Strom sinkt von allein.
2. Nach 12 h wieder 80 % der Nennbetriebsdauer (EN 50171).
3. HV: Batteriebetrieb, alle Leuchten auf 216 V DC aus der Batterie. UV: angeschlossene Leuchten in Dauerlicht, Wechselspannung aus dem Netz der Anlage.
4. Fail-safe: Jede Unterbrechung der Schleife (auch Drahtbruch, defekte DPÜ) schaltet das Licht ein.
5. In betriebsmäßig verdunkelten Räumen geht das Notlicht erst nach manueller Bestätigung aus.
6. Blockieren → Batteriesicherungen ziehen → Netz aus. Blockieren allein macht nichts spannungsfrei.
7. Immer. Zuerst LED „DC OK“, dann Ausgang im DC-Bereich messen (≈ 24 V).
8. Leistung: 7 A × ≈ 250 V ≈ 1.750 W; bei 230 V sind dafür schon > 7 A nötig, dazu die Verluste des Ladeteils (Katalog ≈ 2.100 VA).
</details>

## Praxisauftrag
- [ ] **Ladestrom** am Display ablesen: Erhaltungsladung oder Nachladen?
- [ ] Wie viele **Unterverteilungen** werden überwacht? Gibt es eine **Zener-Abschlussklemme**?
- [ ] **24-V-Netzteil** bzw. +24 V an der Busklemmleiste finden: Leuchtet „DC OK“? Nur schauen, ohne Freigabe nicht messen.

**Nächste Folge:** Stromkreise – Stromkreismodule, Sicherungen und LEDs, 20 Leuchten / 60 %, Joker-Mischbetrieb, Lichtschalterabfrage (LSA), Isolationsmessung Schritt für Schritt.
