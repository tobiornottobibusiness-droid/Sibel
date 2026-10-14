# Begleitheft Folge 2 – Gleichstrom für Wechselstrom-Profis

**Audio:** [folge-02-gleichstrom.mp3](folge-02-gleichstrom.mp3) · **Kapitelmarken:** [kapitel.txt](kapitel.txt) · **Wörtliches Skript:** [skript.md](skript.md)
**Referenzanlage:** INOTEC CPS 220/64 (Werte, die bei der CPS FUSION anders sind, stehen dabei)

## Lernziele
Nach dieser Folge kannst du …
1. erklären, warum LED-Betriebsgeräte Gleich- und Wechselspannung vertragen.
2. die Batterie-Spannungen einordnen (Nenn-, Erhaltungslade-, Starklade-, Ruhe- und Entladeschlussspannung) und pro Zelle umrechnen.
3. erklären, warum die nutzbare Kapazität von der Entladezeit abhängt und warum der Strom am Ende der Entladung steigt.
4. eine Batterie grob überschlagen.
5. die **6 Gleichstrom-Regeln** anwenden.
6. das I-T-Prinzip und die Isolationsüberwachung der Anlage erklären.
7. an Gleichstrom richtig messen (Multimeter, Hall-Zange, Blockspannungen).
8. die Ein- und Ausschaltreihenfolge begründen.

## Spickzettel

### Warum Gleichstrom funktioniert
LED-Betriebsgerät: **Gleichrichter → Glättungskondensator → (PFC) → Stromregler → LEDs**. Liegt am Eingang Gleichspannung an, leiten im Gleichrichter dauerhaft zwei Dioden. Eingangsbereich der Inotec-Module: **220–240 V AC** und ca. **179–264 V DC** (J-SV-Modul; FUSION-FLD: 176–264 V DC).

### 5 Unterschiede AC ↔ DC
1. kein Nulldurchgang → Lichtbögen reißen nicht von selbst ab
2. kein cos φ → P = U · I
3. Polarität zählt
4. Batterie lässt sich nicht abschalten
5. Batteriebetrieb = **nicht geerdetes System** (wie I-T-System) mit Isolationsüberwachung

### Batterie-Spannungen (108 Zellen = 18 Blöcke × 6 Zellen)
| Zustand | pro Zelle | Anlage (×108) | pro 12-V-Block (×6) |
|---------|-----------|---------------|---------------------|
| Starkladung (nach Entladung, IU-Kennlinie) | bis 2,35 V (Ausnahme 2,40 V) | bis ≈ 254–259 V | bis ≈ 14,1–14,4 V |
| **Erhaltungsladung (Normalbetrieb, 20 °C)** | **2,27–2,30 V** | **≈ 245–248 V** ← Display-Rätsel | ≈ 13,6–13,8 V |
| Ruhespannung voll, ohne Ladung | ≥ 2,10 V | ≥ 227 V | ≥ 12,6 V |
| Nennspannung (nur ein Name) | 2,00 V | 216 V | 12 V |
| **Entladeschluss / Tiefentladeschutz CPS 220/64** | ≈ 1,80 V | **194 V** | ≈ 10,8 V |
| Tiefentladeschutz CPS FUSION (laut Anleitung) | ≈ 1,71 V | 185 V | – |
| BCS-Alarm je Block | – | – | < 10,3 V oder > 15,0 V |

- Die genauen Ladespannungen hängen vom Batteriehersteller ab (Datenblatt!).
- **Temperatur:** ideal 20 °C. Ladespannung ≈ −3 mV pro Zelle und Kelvin über 20 °C (temperaturgeführte Ladung über einen Fühler am RIF 5 oder über BCS).
- **Wärme kostet Lebensdauer:** Alterungsreserve nach EN 50171: 25 % bei 20 °C, bei 30 °C über 80 % (verschlossene Batterien).
- Tiefentladeschutz ausgelöst → **am Steuerteil quittieren**. Ursache klären, Batterie laden.

### Ampere-Stunden, Wattstunden, Leistung
- **Ah = A × h.** Kapazitätsangabe meist C10 (10-h-Entladung bis 1,8 V/Zelle).
- **Kapazität hängt von der Entladezeit ab.** Beispiel Inotec-Batterie 12 Ah:

  | Entladezeit | Strom | entnehmbar |
  |---|---|---|
  | 8 h | 1,3 A | ≈ 10,4 Ah |
  | 3 h | 3,0 A | ≈ 9 Ah |
  | 1 h | 6,3 A | ≈ 6,3 Ah |
- **Wh = V × Ah:** 216 V × 12 Ah ≈ 2,6 kWh. Muster-EltBauVO: Notlichtsysteme mit verschlossenen Batterien ≤ 2 kWh (≈ 216 V/9,2 Ah) sind ausgenommen; bis 20 kWh (≈ 216 V/92 Ah) Erleichterungen bei der Lüftung.
- **DC-Leistung:** P = U · I (im Netzbetrieb haben LED-Geräte cos φ ≈ 0,85–0,98, deshalb stehen in Datenblättern VA-Angaben).
- **Konstante Leistung → Strom steigt bei sinkender Spannung:** 1.000 W bei 216 V ≈ 4,6 A, bei 194 V ≈ 5,2 A.
- **Überschlag:** 100 Leuchten × 5 W = 500 W → 500 W / 216 V ≈ 2,3 A → +25 % Alterung ≈ 2,9 A → Tabelle 3 h: Typ 20-12 schafft 3,0 A (knapp). In der Praxis rechnen Planer bzw. Konfigurator, du prüfst auf Plausibilität.
- **Laden:** 80 % der Betriebsdauer nach 12 h (EN 50171). Betriebsdauertest deshalb nur zu risikoarmen Zeiten.

### Die 6 Gleichstrom-Regeln
| # | Regel | Konsequenz |
|---|-------|------------|
| 1 | **Der Lichtbogen geht nicht von allein aus** (kein Nulldurchgang) | Nie unter Last trennen. Vorher blockieren. Nur DC-bemessene Schaltgeräte. Nur **Originalsicherungen mit Löschmittel** (1.500 A Abschaltvermögen; CP 4x2A = 3,15 A, CP 2x4A = 6,3 A, CP 1x6A = 10 A) |
| 2 | **Die Batterie kann man nicht ausschalten** | Batteriesicherungen trennen nur das Gerät, der Strang bleibt bei ≈ 245 V. Ein 12-V-Block liefert mehrere hundert Ampere Kurzschlussstrom. **Isoliertes Werkzeug**, kein Schmuck, Polkappen, Schutzbrille, Freigabe. Wasserstoff → keine Funken, Lüftung. > 120 V DC → Zugang beschränkt |
| 3 | **Im Notbetrieb ist der N kein Neutralleiter** | L = Plus, N = Minus, System nicht geerdet. Spannungsfreiheit **allpolig** feststellen (L–N, L–PE, N–PE) mit einem DC-fähigen zweipoligen Prüfer |
| 4 | **Der Stromkreis wird von woanders eingeschaltet** | UV abschalten → DPÜ meldet → Sicherheitsleuchten gehen AN. Automatischer Funktionstest jederzeit möglich. **An der Anlage freischalten** nach Betriebsanweisung: lastfrei machen → allpolig trennen → sichern → allpolig prüfen. Blockieren ist **keine** sichere Trennung. Betreiber informieren, Prüfbuch |
| 5 | **Gleichstrom ist nicht harmlos** | Herz-Flimmerschwelle zwar höher, Loslassen leichter (IEC 60479-1), Grenze Berührungsspannung 120 V DC statt 50 V AC, aber die Anlage arbeitet mit ≈ 245 V. Dazu Lichtbögen und Kurzschlussströme |
| 6 | **Die Polarität zählt** | Batteriepolarität **vor** dem Einsetzen der Batteriesicherungen prüfen. Stromkreise L+/N− polrichtig (bei FUSION sonst Kommunikationsprobleme) |

### Isolationsüberwachung (I-T-Prinzip)
- **1. Fehler** (z. B. Feuchte in einer Außenleuchte, Plus gegen PE): kein Fehlerstrom, Licht läuft weiter, die Anlage meldet einen **Isolationsfehler (< 470 kΩ)**. Gemessen wird im Batteriebetrieb (FT, BT, Netzausfall).
- **2. Fehler** am anderen Pol: Kurzschluss bzw. gefährliche Berührungsspannung. → Isolationsfehler **zeitnah beheben**.
- Fehler können an beiden Polen auftreten → DC-Kreise **2-polig absichern**.
- **ISO-Test** (halbjährlich) prüft nur die Messeinrichtung, keine Isolationsmessung.
- **Isolationsmessung** vor der Inbetriebnahme: System freischalten, **L+N brücken**, gegen PE messen, **max. 500 V DC**, **nie an 24-V-Kreisen**.

### Messen an Gleichstrom
- **Multimeter:** DC-Bereich. Minuszeichen = Messspitzen vertauscht (hilft beim Pole-Finden).
- **Strom:** Eine normale Zange (Wandlerprinzip) zeigt bei DC **null**. Du brauchst eine **AC/DC-Zange mit Hall-Sensor**. **Nullabgleich** vor jeder Messung.
- **Blockspannungen** untereinander vergleichen (Erhaltungsladung ≈ 13,6–13,8 V). Ein Ausreißer ist verdächtig: Ein schwacher Block gefährdet den ganzen Strang (Reihenschaltung).

### Schaltreihenfolge (angewandte Gleichstromphysik)
- **Ein:** Netz → Ladeteil → Batteriesicherungen (vorher Polarität prüfen)
- **Aus:** Blockieren (NL + DL) → Batteriesicherungen raus → Netz aus
- Warum: Nach dem Blockieren fließt kein Laststrom, beim Ziehen entsteht also kein DC-Lichtbogen, und die Leuchten gehen beim Netz-Aus nicht auf Batterie.

## Selbsttest
1. Zellenzahl? Warum zeigt das Display ≈ 245 V statt 216 V?
2. Tiefentladeschutz der CPS 220/64 in Volt und pro Zelle?
3. Warum liefert eine 12-Ah-Batterie in 1 h nur ≈ 6 Ah?
4. Warum steigt der Batteriestrom gegen Ende der Entladung?
5. Warum ist ein DC-Lichtbogen gefährlicher?
6. Im Batteriebetrieb liegt zwischen N und PE eine Spannung. Fehler?
7. Du schaltest für Arbeiten an einer Sicherheitsleuchte die UV ab. Was passiert, und wie geht es richtig?
8. *(Bonus)* Warum ersetzt der ISO-Test keine Isolationsmessung?

<details><summary>Antworten</summary>

1. 108 Zellen. Erhaltungsladung mit 2,27–2,30 V/Zelle; 216 V ist nur die Nennspannung.
2. 194 V ≈ 1,8 V/Zelle (FUSION: 185 V).
3. Die nutzbare Kapazität sinkt bei hohen Entladeströmen, die Chemie kommt nicht hinterher.
4. Die Betriebsgeräte ziehen konstante Leistung, I = P/U.
5. Kein Nulldurchgang, der Bogen reißt nicht ab.
6. Nicht zwingend. Der N ist im Batteriebetrieb der Minuspol eines ungeerdeten Systems. Allpolig prüfen.
7. Die DPÜ meldet einen Netzausfall UV, die Sicherheitsleuchten gehen an. Richtig: an der CPS lastfrei machen, allpolig trennen nach Betriebsanweisung, sichern, allpolig prüfen, Betreiber informieren.
8. Er prüft nur die eingebaute Messeinrichtung (Simulation), nicht die Isolation der Leitungen.
</details>

## Praxisauftrag
- [ ] Batteriespannung am Display ablesen, **÷ 108** rechnen. Liegt der Wert bei 2,27–2,30 V/Zelle? Temperaturfühler oder BCS vorhanden?
- [ ] **Prüfbuch:** Hat der letzte Betriebsdauertest die volle Nennbetriebsdauer geschafft?
- [ ] **Werkzeug-Check:** Zeigt dein Spannungsprüfer DC an? Gibt es eine AC/DC-Zange (Hall)? Gibt es isoliertes Werkzeug für die Batterie?
- [ ] Einen erfahrenen Kollegen fragen, **wie im Betrieb ein SiBe-Stromkreis freigeschaltet wird**, und mit den 6 Regeln vergleichen.
