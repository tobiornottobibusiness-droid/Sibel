# Begleitheft Folge 4 – Die Anlage lesen: CPS 220/64 von außen nach innen

**Audio:** [folge-04-anlage-lesen.mp3](folge-04-anlage-lesen.mp3) · **Kapitelmarken:** [kapitel.txt](kapitel.txt) · **Wörtliches Skript:** [skript.md](skript.md)
**Ausführlich:** [wissensbasis/04-cps-220-64.md](../../wissensbasis/04-cps-220-64.md) (Abschnitt 8), [Glossar: Betriebsmittelkennzeichen](../../wissensbasis/03-glossar.md), [Praxisbeispiel Kaufel viaFlex](../../wissensbasis/06-praxisbeispiel-kaufel-viaflex.md) · Lernmaterial, ersetzt weder Herstelleranleitung noch Betriebsanweisung

## Lernziele
Nach dieser Folge kannst du …
1. ein Typenschild lesen und auf Plausibilität prüfen (Spannung pro Zelle, Anlagengröße).
2. die Typenbezeichnung der CPS 220/64 entschlüsseln.
3. die Bereiche im Schrank und die Klemmleisten X1, X2, X3 (+ X4, X5, X8) zuordnen.
4. Betriebsmittelkennzeichen lesen (Vorzeichen, Kennbuchstabe, Zählnummer) und weißt, warum die Legende im Plan entscheidet.
5. mit der Methode **„vom Verbraucher zur Quelle“** die richtige Trennstelle finden.

## Spickzettel

### Drei Informationsquellen + Messgerät
**Typenschild → Beschriftung (Kennzeichen, Klartext) → Plan → nachmessen.** Erst lesen, zuordnen, messen, dann handeln.
⚠️ Eine Sicherung, deren Aufgabe du nicht kennst, ziehst du nicht (dahinter kann z. B. die Netzüberwachung eines ganzen Bereichs hängen).

### Typenschild
| Angabe | Wozu |
|---|---|
| Gerätetyp + Gerätenummer (INOTEC: **KA…**) | Hotline; Download der Standarddoku (Gehäuseansichten, Stromlaufpläne, Klemmenpläne) auf inotec-licht.de mit Serien-/Auftragsnummer |
| Batterie: Spannung, Zellenzahl, Typ, Kapazität | Plausibilität: Kaufel 259,2 V ÷ 108 Zellen = **2,4 V/Zelle** = Starkladung |
| Netz, Vorsicherung, Ladestrom, Leistung/Verbraucherstrom, Nennbetriebsdauer, Norm EN 50171 | Anlagengröße einschätzen |

**Typenbezeichnung `CPS 220/64/11kW-1 3-ph`:**
| Teil | Bedeutung |
|---|---|
| CPS | Zentralbatteriesystem |
| 220 | Systemspannung (Batterie 216 V) |
| 64 | max. Stromkreise im Hauptschrank = 16 Steckplätze × 4 (`/20` = 5 × 4, `/8` = 2 × 4); mit Unterstationen bis 128 |
| 11kW | max. Anschlussleistung |
| -1 / -2 | ein oder zwei Ladeteile (laut Typenliste) |
| 1-ph / 3-ph | Netzanschluss |

**Jedes Gerät hat ein eigenes Typenschild:** 24-V-Netzteil (z. B. Mean Well DR-60-24: Ausgang **24 V DC, 2,5 A**) ≠ Ladeteil (arbeitet auf Batteriespannung ≈ 240 V, nennt einen **Ladestrom**).

### Der Schrank (CPS 220/64, 11 kW)
| Bereich | Inhalt |
|---|---|
| Tür („Armaturenbrett“) | Steuerteil 5,7" TFT-Touch, Dokumententasche innen |
| Kabeleinführung | meist oben, Schiebeblech oder Verschraubungen; Klemmleisten in der Nähe |
| 19"-Baugruppenträger | Stromkreis-Einschübe (CP 4x2A …) mit eigenen Sicherungen und LEDs; Nummer **Einschub.Stromkreis** (4.1); 24-V-Einschübe belegen 2 Plätze, von rechts nach links |
| Ladeteile, Optionen (TE) | LT 1,2 / 3 / 7 A; RIF 5, DPÜ, LSA, BCS, Sicherungsabgänge für Unterstationen |
| Sicherungen | Netzeingangssicherung (X1), Batterieabsicherung + / − |
| Batterieschrank | bei 11 kW unten, mit dem Elektronikschrank verschraubt (zusammen 2.030 mm hoch); große Anlagen: separates Gestell |

LEDs am Einschub (Details Folge 7): rot dauernd = Leuchtenstörung · gelb = Dauerlicht ein · alle 4 rot schnell blinkend = Busstörung.
Neue Anlage: Schutzabdeckung auf dem obersten Baugruppenträger **vor dem Einschalten entfernen**.

### Klemmleisten – „Strom rein, reden, Licht raus“
| Leiste | Inhalt |
|---|---|
| **X1** | Netz: Netzeingangssicherung + N, PE. Bei 3~ DPÜ eingebaut (an RIF 5). Ladeteil 7 A zieht ≈ 9 A, 3 A ≈ 4 A, 1,2 A ≈ 2 A |
| **X2** | Busse: IB2 (IB2, ⊥, +24 V), IB3 (nur DPÜ/B.2), RTG (R, T, G); max. 500 m, mind. 0,5 mm² |
| **X3** | Endstromkreise 230 V: L, N, PE |
| X4 | D.E.R.: L+, N−, B+, B− |
| X5 | 24-V-Kreise |
| X8 | RIF 5, LSA 8.1, DPÜ; MTB über RIF-5-Kontakte |
| Batterie | an Batterieabsicherung + / −: **blockieren → Batteriesicherungen raus → anschließen, Polung prüfen**, isoliertes Werkzeug, 216 V DC |
| Unterstationen | CPUSB: Sicherungsabgang L+/N− + Bus IB2 · CPUS: Netz- **und** Batterieleitung (Batterie in Funktionserhalt; Netz ggf. aus der UV vor Ort) |

⚠️ Ein Kreis an X3 ist **nicht spannungsfrei, nur weil das Licht aus ist** (Netzbetrieb AC, Notbetrieb DC, Funktionstest schaltet jederzeit ein).

### Betriebsmittelkennzeichen
`=` Anlage/Funktion · `+` Ort · `-` Betriebsmittel (**kein Minuspol!**)

| Buchstabe | Bedeutung |
|---|---|
| **F** | Schutz: Sicherung, LS-Schalter |
| **X** | Klemme, Stecker |
| **A** | Baugruppe, Modul |
| **K** | Relais, Überwachungsrelais (ältere Pläne auch Schütz) |
| **Q** | Schalter für Energie, z. B. Lasttrennschalter (neuere Pläne auch Schütz) |
| **G** | Energiequelle (Batterie; je nach Plan Netzteil) |
| **T** | Transformator, Umformer (je nach Plan Netzteil) |

- Normausgaben haben Buchstaben geändert → **verbindlich ist die Legende im Plan.**
- Gleiche Nummer = gehört oft zusammen: Kaufel **-A101** (Unterstation US 10) ↔ **-F101** (ihre AC-Sicherung).
- **Gleiches Kennzeichen, anderer Ort:** -F101 ist in der Kaufel-Zentrale die **Netzsicherung**. Erst der Ort (`+`) macht es eindeutig.
- Stromkreislegende: `41F3` = 3. Abgang hinter Vorsicherung `F41`. „-K03 … Spannungsüberwachung“ = Netzwächter → **nicht abschalten** (sonst Netzausfall-Meldung, Notlicht an).
- Buchstabe = *was*, Nummer = *welches*, Klartext = *wofür*, **Plan = woher der Strom kommt**.

### Den Plan lesen
| Dokument | Zeigt |
|---|---|
| Gehäuseansicht | wo was sitzt |
| Stromlaufplan | wie es verschaltet ist |
| Klemmenplan | welche Ader an welcher Klemme |
| Leuchtenliste / Anschlussplan Endstromkreise | Einschub, Kreis, Überwachung, Kabel-Nr., Schaltungsart, Zielort, Strom |
| Übersichtsplan Gebäude | Zentrale → Stränge → E30-Kästen → Unterverteiler |

Kabel: **NHXH-J … E30** = Funktionserhalt · **NYM-J** = normale Installationsleitung · **J-Y(St)Y** = Fernmelde-/Datenleitung. Farben im Plan sind projektabhängig → Legende.
Plan passt nicht zur Anlage (z. B. Gessler: Typenschild 15 Ah, verbaut 18 Ah)? **Es gilt, was du misst.** Abweichung dokumentieren und dem Betreiber melden.

### Methode „vom Verbraucher zur Quelle“
1. Am Gerät: Kennzeichen und Anschlussbeschriftung lesen, **Einspeisungen zählen**.
2. Im Plan jede Einspeisung bis zur Schutzeinrichtung zurückverfolgen.
3. Die Stelle im Gebäude suchen, Schild und Nummer vergleichen.
4. **Was hängt noch dran?** Mehrere Unterstationen/Bereiche → mit verantwortlicher EFK und Betreiber abstimmen.
5. Freischalten, gegen Wiedereinschalten sichern, **allpolig prüfen** (an **UC-Eingängen AC und DC**, gegen PE **und** zwischen den Polen).
6. Dokumentieren, Gegenprobe: Nachbarn laufen weiter.

Rückwärts genauso: Störmeldung „Kreis 4.2, Leuchte 7“ → Leuchtenliste → Zielort und Kabelnummer → Leuchte im Gebäude.

### Praxisfall Kaufel viaFlex: Unterstation US 10 tauschen
| Schritt | Ergebnis |
|---|---|
| -F101 im Unterverteiler raus | AC-Seite von US 10 spannungsfrei ✔ |
| UC gemessen | weiter **230 V AC** (Netzbetrieb) |
| -F100.1 / -F100.2 raus | UC unverändert → **falsche Trennstelle** |
| Plan gelesen: Unterverteiler hängt über E30-Kasten am Strang | E30-Kasten „SIBEL Strang 11“ mit **UC+ / UC−** |
| UC+ / UC− raus | < 2 V AC/DC gegen Erde ✔ (zwischen den Polen auch messen!) |
| Wieder ein: UC zuerst, dann -F101 | Deckel E30-Kasten fest verschrauben |

### Transfer-Ecke
| | INOTEC CPS 220/64 | Gessler SiBELON | Kaufel viaFlex |
|---|---|---|---|
| Netz | Netzeingangssicherung an X1 | -2F1 „Netz“ | -F101 … -F103 |
| Batterie | Batterieabsicherung + / − | -2F4 / -2F5 „Batterie + / −“ | -F111 (+) / -F112 (−) |
| Laden | Ladeteile LT | -2F10.1 / -2F10.2 „Ladung DC“ | Ladetransformatoren im Schrank |
| Busse | IB1/IB2/IB3, RTG | SPS (SETLON, WAGO-System) | LON |
| Unterstation | CPUSB: L+/N−/PE + IB2 | – | US: **UC** aus der CPS + **AC** aus dem Gebäude |

**Frage für deinen nächsten Schrank:** Wie heißen hier die Batteriesicherungen, und wo steht das?

## Selbsttest
1. Welche zwei Angaben vom Typenschild will die Hotline?
2. Was bedeutet die 64 in CPS 220/64?
3. Was hängt an X1, X2, X3?
4. Woran unterscheidest du ein 24-V-Netzteil von einem Ladeteil?
5. Warum ist „-F101“ allein nicht eindeutig?
6. Die Methode „vom Verbraucher zur Quelle“ in Stichworten?
7. Warum misst du an einem UC-Eingang AC **und** DC?
8. *(Bonus)* Was bedeutet das Minus vor „-F101“?

<details><summary>Antworten</summary>

1. Gerätetyp und Gerätenummer (INOTEC: KA…).
2. Bis zu 64 Stromkreise im Hauptschrank (16 Einschübe × 4).
3. X1 Netz, X2 Busse, X3 Leuchten: „Strom rein, reden, Licht raus“.
4. Am eigenen Typenschild: Netzteil = Ausgang 24 V; Ladeteil = Batteriespannung und Ladestrom. Im Zweifel Plan.
5. Dasselbe Kennzeichen kann es in mehreren Schränken geben (Kaufel: Zentrale = Netz, Unterverteiler = AC-Sicherung US 10). Erst der Ort macht es eindeutig; Buchstabenbedeutung laut Legende des Plans.
6. Kennzeichen lesen, Einspeisungen zählen → im Plan zur Sicherung verfolgen → vor Ort suchen und vergleichen → was hängt noch dran, abstimmen → freischalten, sichern, allpolig prüfen → dokumentieren, Gegenprobe.
7. UC = Allstrom: im Netzbetrieb AC, im Notbetrieb DC. Nur eine Messart → evtl. 0 V angezeigt, obwohl Spannung anliegt.
8. Es kennzeichnet ein Betriebsmittel (Produktaspekt), kein Minuspol. `=` = Anlage, `+` = Ort.
</details>

## Praxisauftrag
- [ ] **Typenschild** der nächsten Anlage fotografieren und entschlüsseln: Typ, Zellenzahl, Spannung pro Zelle, Nennbetriebsdauer.
- [ ] **Klemmleisten** für Netz, Busse, Leuchten und die **Batteriesicherungen** finden und im Plan wiederfinden.
- [ ] **Einen Endstromkreis auf dem Papier verfolgen:** Zielort → Kabelnummer → Einschub → Klemme. Nur lesen, nichts anfassen.

**Nächste Folge:** Die Batterie in der Praxis – Bauarten, Alterung, Temperatur, Tiefentladeschutz, Einzelblocküberwachung, Inspektion und Batterietausch.
