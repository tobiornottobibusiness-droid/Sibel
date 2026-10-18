# Begleitheft Folge 7 – Stromkreise

**Audio:** [folge-07-stromkreise.mp3](folge-07-stromkreise.mp3) · **Kapitelmarken:** [kapitel.txt](kapitel.txt) · **Wörtliches Skript:** [skript.md](skript.md)
**Ausführlich:** [wissensbasis/04-cps-220-64.md](../../wissensbasis/04-cps-220-64.md) (Abschnitt 3, 4, 10), [wissensbasis/01-cps-fusion-anlage.md](../../wissensbasis/01-cps-fusion-anlage.md) (Abschnitt 7) · Lernmaterial, ersetzt weder Herstelleranleitung noch Betriebsanweisung

## Lernziele
Nach dieser Folge kannst du …
1. die Stromkreismodule der CPS 220/64 (und der FUSION) zuordnen und ihre LEDs lesen.
2. Sicherungen, Einschaltstrom und die Regel „20 Leuchten / 60 %“ erklären und nachrechnen.
3. die Brandabschnitts-Regel anwenden.
4. Überwachungsarten, Joker-Mischbetrieb und Lichtschalterabfrage (LSA) erklären.
5. eine Isolationsmessung an einer CPS korrekt durchführen und weißt, wo du **nicht** messen darfst.

## Spickzettel

### Stromkreismodule („Stromkreisumschaltungen“)
Im Netzbetrieb 230 V AC, im Batteriebetrieb 216 V DC auf den Kreis. Betriebsgeräte können beides → **kein Wechselrichter**.

| Modul (CPS 220/64) | Kreise | Last je Kreis | Sicherung (Original mit Löschmittel) | 60 % davon |
|---|---|---|---|---|
| CP 4x2A | 4 | 2 A | 3,15 A | ≈ 1,9 A |
| CP 2x4A | 2 (nur x.1/x.2) | 4 A | 6,3 A | ≈ 3,8 A |
| CP 1x6A | 1 (nur x.1) | 6 A | 10 A | 6 A |
| CP 2x2,5A/24V | 2 (SELV) | 2,5 A | 5 AT | – |
| CP D.E.R. 2x2,5A | 2 + Bus B+/B− | 2,5 A | 3,15 A | – |

- FUSION: CF 4x1A / 2x2,5A / 1x5A.
- Abschaltvermögen 1.500 A; **max. Einschaltstrom 250 A / 500 µs** je Kreis.
- Nummer **Einschub.Stromkreis** (4.1). Leuchten an **X3** (L, N, PE). 24-V- und D.E.R.-Module belegen 2 Plätze, von rechts nach links.
- D.E.R. an der 220/64: Busleitung B+/B− (500 m bei 0,5 mm², 2.000 m bei 1,5 mm²), Adressen Kreis 1 = 1–20, Kreis 2 = 21–40. FUSION: ohne Busleitung.
- Externe Module in Bus-Unterstationen: Versorgung L+/N−/PE in Funktionserhalt + Bus → bis 128 Kreise.
- ⚠️ **Module nur spannungsfrei wechseln.**

| LED am Modul | Bedeutung |
|---|---|
| rot dauernd | Leuchtenstörung |
| rot, 1 LED blinkt alle 3 s | Überlast in diesem Kreis |
| rot, blitzt (0,5 s) | keine Ausgangsspannung (z. B. Sicherung ausgelöst → erst Ursache suchen) |
| alle 4 rot schnell blinkend | Busstörung |
| gelb | Dauerlicht ein |

### Regeln für Endstromkreise (VDE V 0100-560-1)
- **≤ 20 Leuchten** und **≤ 60 %** des Sicherungsnennstroms.
- Spannungsfall **≤ 4 %**. Batteriebetrieb: 194 V − 4 % ≈ 186 V an der letzten Leuchte; J-SV arbeitet ab 179 V DC → passt, aber zu lange/dünne Leitungen lassen die letzte Leuchte vor Ende der Nennbetriebsdauer ausgehen.
- **Keine AFDD**. RCD nur, wenn nötig, dann **einer je Stromkreis**.
- DC-Kreise **2-polig** absichern.

### Brandabschnitte
- Ab **2 Leuchten je Brandabschnitt** abwechselnd auf **mind. 2 Stromkreise**, **jeder im eigenen Kabel** → bei Ausfall bleibt jede zweite Leuchte an („Lichterkette“).
- Ein Endstromkreis versorgt Leuchten nur in **einem** Brandabschnitt; Leitungen durch mehrere Brandabschnitte brauchen Funktionserhalt.
- Prüfen über Leuchtenliste (Stromkreis + Zielort). Alle Leuchten eines Brandabschnitts an einem Kreis = Mangel → Betreiber.

### Überwachung und Joker
| Überwachungsart | Wie | Ergebnis |
|---|---|---|
| unüberwacht | – | keine Meldung |
| Stromkreisüberwachung | Strom des Kreises gegen Referenz (**Learn-Mode**) | „Fehler im Kreis“, aber nicht welche Leuchte |
| Einzelleuchtenüberwachung | Modul mit Adresse je Leuchte | genaue Leuchte |

- **Joker** (INOTEC-Patent): DL und BL gemischt in einem Kreis, ohne Datenleitung. Am Joker-EVG / J-SV-Modul: **Mikroschalter** = Schaltungsart, **Adressschalter** = Adresse 1–20, optional **Sense-Eingang** (lokal schalten, z. B. Raumlichtschalter).
- J-SV erkennt: Betrieb > 20 mA, Fehler < 10 mA.
- ⚠️ **Schaltungsart gilt nur im Netzbetrieb.** Netzausfall UV (überwacht): **alle** Leuchten aller Kreise an (Netz aus der CPS). Netzausfall HV: alles auf Batterie.
- FUSION: feste ID statt Schalter, Schaltungsart je Leuchte am Steuerteil, **Einzel-LED-Überwachung** (> 97 % der LED-Defekte sind Kurzschlüsse), Dauerlicht permanent überwacht, **Stromkreisprüfung** (hängt jedes Gerät am richtigen Kreis?).
- Nach jeder behobenen Leuchtenstörung: **Funktionstest**. Nach Leuchtentausch: Einstellungen wie alt (Joker) bzw. **neu einlernen**.

### Lichtschalterabfrage (LSA)
Sicherheitsleuchten gehen **mit der Allgemeinbeleuchtung** an (geschaltetes Dauerlicht: im Netzbetrieb per Schalter, bei Netzausfall immer an). BL/gedimmt → ein, DL bleibt an. Bis zu **3 Schalteingänge** je Kreis. Invertierter Eingang: Kreis gezielt bei Phasenausfall ein.

| | LSA 3.1 | LSA 8.1 |
|---|---|---|
| Anzahl je Steuerteil | max. 8 | max. 3 |
| Eingänge | 3 | 8, **galvanisch getrennt** |
| Bus | **nur IB2** | IB2/IB3 |
| Besonderheit | **nur ein gemeinsamer N** für L1–L3 (230-V-Version) | integrierte DPÜ/B (gleiche Adresse) |
| Varianten | 24 V DC / 230 V AC | 24 V DC / 230 V AC |

Jedes Modul: eindeutige Adresse am Adressschalter, im Steuerteil aktiv setzen.

### Isolationsmessung Schritt für Schritt (MAN 708199, Kap. 7.2)
1. **Komplettes System freischalten** (Netz **und** Batterie) nach Anleitung/Betriebsanweisung, **gegen Wiedereinschalten sichern**.
2. **L und N des Endstromkreises brücken.**
3. Messen **nur PE gegen L** und **PE gegen N**, **max. 500 V DC, 1 mA**, Messgerät nach **DIN VDE 0413**. Mindestwert nach DIN VDE 0100-600 (Kreise bis 500 V): **≥ 1 MΩ**.
4. **Brücke entfernen**, nächster Kreis (1.1, 1.2 … und alle Kreise der Unterstationen).
5. Erst nach Abschluss aller Messungen wieder einschalten.

⚠️ **Nie an Stromkreisen mit INOTEC-24-V-Leuchten messen (auch nicht CPUSB-24-V-Kreise): die Leuchten werden zerstört.**
**Protokoll:** Kreisnummer, Messspannung, Wert, Datum, Messgerät, Name, und welche Kreise bewusst nicht gemessen wurden.

### Isolationsüberwachung im Betrieb
- Im Batteriebetrieb (FT, BT, Netzausfall) überwacht, Meldung bei **< 470 kΩ** (Batterie ungeerdet, I-T-Prinzip).
- „Isolationsfehler +“ = Pluspol–PE, „−“ = Minuspol–PE. Ursache kann jede mit der Batterie verbundene Komponente sein (Leuchte, LSA 8, DPÜ/B …).
- **ISO-Test** (halbjährlich) prüft nur die Messeinrichtung (Simulation), **ersetzt keine Isolationsmessung**.
- Fehlersuche: freischalten, Kreise über die Trennklemmen einzeln messen. Typisch: Feuchtigkeit in Außenleuchte oder Abzweigdose.

### Transfer-Ecke
| | Gessler SiBELON | Kaufel viaFlex |
|---|---|---|
| Kreise | 20 Endstromkreise F1–F20, je rote + blaue Sicherungsklemme (**2-polig**); „20S“ im Typ vermutlich = 20 Stromkreise | 2 Kreise je Unterstation (Circuit 1/2), Klemmen C1+/C1−/C2+/C2− (**2-polig**) |
| Beispiel | – | US 10: Kreis 7 mit 13 Leuchten, Kreis 8 mit 8 Leuchten (beide ≤ 20) |
| Leuchtenadressen | – | adressierbare **FLX**-Bausteine → nach US-Tausch Leuchten suchen; „FLX-Ströme zurücksetzen“ erinnert ans Neu-Einlernen |

**Frage für deinen nächsten Einsatz:** Liegen die Leuchten in einem Brandabschnitt abwechselnd auf mindestens zwei Kreisen? Wie viele Leuchten hängen am vollsten Kreis der Anlage?

## Selbsttest
1. Warum braucht eine CPS keinen Wechselrichter?
2. Was bedeutet eine rote LED, die alle 3 s blinkt?
3. Warum nur Originalsicherungen mit Löschmittel?
4. Regel für Endstromkreise und Regel für Brandabschnitte?
5. Gilt die eingestellte Schaltungsart auch bei Netzausfall?
6. Was macht die Lichtschalterabfrage?
7. Schritte der Isolationsmessung und die wichtigste Ausnahme?
8. *(Bonus)* Warum ist der Spannungsfall im Batteriebetrieb besonders kritisch?

<details><summary>Antworten</summary>

1. Die Betriebsgeräte vertragen AC und DC; das Modul schaltet nur zwischen Netz und Batterie um.
2. Überlast in diesem Stromkreis.
3. Im Batteriebetrieb fließt Gleichstrom, der Lichtbogen erlischt nicht von selbst; die Sicherung muss bei 216 V DC mit hohem Abschaltvermögen (1.500 A) sicher trennen.
4. ≤ 20 Leuchten, ≤ 60 % des Sicherungsnennstroms. Ab 2 Leuchten je Brandabschnitt abwechselnd auf mind. 2 Kreise, jeder im eigenen Kabel.
5. Nein, nur im Netzbetrieb. Bei Netzausfall gehen alle Leuchten an.
6. Schaltet Sicherheitsleuchten zusammen mit der Allgemeinbeleuchtung (Lichtschaltersignal über den Bus).
7. Freischalten + sichern, L und N brücken, nur PE gegen L und N mit max. 500 V DC, Brücke raus, nächster Kreis. **Nie an 24-V-Kreisen.**
8. Am Ende der Entladung liegt die Batterie bei ≈ 194 V; mit 4 % Spannungsfall bleiben ≈ 186 V, das J-SV braucht ≥ 179 V DC. Mehr Spannungsfall → letzte Leuchte geht vor Ende der Nennbetriebsdauer aus.
</details>

## Praxisauftrag
- [ ] **Module ansehen:** Welche Typen sind verbaut? Leuchtet irgendwo eine rote oder gelbe LED?
- [ ] **Leuchtenliste:** In einem Brandabschnitt (z. B. Flur) abwechselnd auf zwei Kreisen?
- [ ] **Messprotokoll** der letzten Isolationsmessung suchen: Werte je Kreis? 24-V-Kreise ausgenommen?

**Nächste Folge:** Leuchten und Betriebsgeräte – Rettungszeichen vs. Sicherheitsleuchte, Erkennungsweite und Montagehöhe, Joker-EVG/J-SV-Modul, Leuchtentausch und Einlernen, LED-Fehlerbilder.
