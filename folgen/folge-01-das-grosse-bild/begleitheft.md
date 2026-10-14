# Begleitheft Folge 1 – Das große Bild

**Audio:** [folge-01-das-grosse-bild.mp3](folge-01-das-grosse-bild.mp3) · **Kapitelmarken:** [kapitel.txt](kapitel.txt) · **Wörtliches Skript:** [skript.md](skript.md)

## Lernziele
Nach dieser Folge kannst du …
1. Notbeleuchtung, Ersatzbeleuchtung und Sicherheitsbeleuchtung (mit ihren drei Unterarten) unterscheiden.
2. erklären, was eine Rettungszeichenleuchte und was eine Sicherheitsleuchte ist.
3. die Kernzahlen 1 lx / 0,5 lx / 15 lx einordnen.
4. Umschaltzeit und Nennbetriebsdauer erklären und Beispiele nennen.
5. Dauerlicht, Bereitschaftslicht und geschaltetes Dauerlicht unterscheiden.
6. „Netzausfall Hauptverteiler“ und „Netzausfall Unterverteiler“ auseinanderhalten.
7. Einzelbatterie, LPS und CPS vergleichen.
8. die **5 Bausteine** einer Zentralbatterieanlage aufzählen und erklären, warum keine Wechselrichter nötig sind.

## Spickzettel

### Begriffsbaum (DIN EN 1838)
```
Notbeleuchtung
├── Ersatzbeleuchtung ............ weiterarbeiten (OP, Leitwarte)
└── Sicherheitsbeleuchtung ....... Menschen sicher raus
    ├── für Flucht- und Rettungswege ....... ≥ 1 lx auf dem Boden
    ├── Antipanikbeleuchtung ............... ≥ 0,5 lx (große Flächen)
    ├── für Arbeitsplätze mit bes. Gefährdung  10 % der Allgemeinbel., mind. 15 lx
    └── Sicherheitszeichen (Rettungszeichenleuchten)
```
- **Rettungszeichenleuchte** = grünes, hinterleuchtetes Piktogramm. Sie **zeigt** den Weg.
- **Sicherheitsleuchte** = leuchtet den Boden aus. Sie macht den Weg **sichtbar**.
- **Größenordnung:** Büro ≈ 500 lx · Sicherheitsbeleuchtung Rettungsweg ≥ 1 lx · Vollmondnacht ≈ 0,1–0,3 lx.
- Sicherheitsbeleuchtung ist immer **zusätzlich** zur Allgemeinbeleuchtung da. Je Bereich **mindestens 2 Leuchten**.

### Wer schreibt was vor?
| Ebene | Was | Beispiele |
|-------|-----|-----------|
| Recht: **ob** | Baurecht (Sonderbauten) und Arbeitsschutz (Gefährdungsbeurteilung) | Versammlungsstätte > 200 Besucher, Verkaufsstätte > 2.000 m², Beherbergung > 12 Gastbetten, Hochhaus, Schule, Großgarage, Krankenhaus |
| Normen: **wie** | DIN EN 1838 = Licht · DIN EN 50172 = Anlage & Prüfung · DIN EN 50171 = Gerät (CPS/LPS) | Details in Folge 3 |
| Prüfung | Prüfbuch für jede Prüfung; in Sonderbauten alle **3 Jahre** Prüfsachverständige | – |

### Umschaltzeit und Nennbetriebsdauer (Beispiele, Deutschland)
| Gebäude | Umschaltzeit | Nennbetriebsdauer (bewährte Werte nach DIN VDE V 0108-100-1) |
|---------|--------------|------------------------------------|
| Versammlungsstätte (Kino, Theater) | 1 s | 3 h |
| Verkaufsstätte | 1 s | 3 h |
| Schule | 15 s | 3 h |
| Hotel, Heim | 15 s (1–15 s) | 8 h |
| Rettungswege in Arbeitsstätten | siehe ASR A2.3 | 1 h |
- Europäische Grundregel (EN 1838): 50 % nach 5 s, 100 % nach 60 s; Systembetriebsdauer mind. 1 h.
- Die neue DIN EN 50172:2024-10 nennt die Betriebsdauern nur noch als Empfehlung. Das Baurecht (VV TB) verweist aber weiter auf DIN VDE V 0108-100-1. INOTEC empfiehlt deshalb, **bis auf Weiteres die bewährten Werte** anzuwenden. Im Zweifel gelten Baugenehmigung und Brandschutzkonzept.
- Die Nennbetriebsdauer wird **im Steuerteil eingestellt**.

### Schaltungsarten
| Schaltungsart | Alltag | Netzausfall |
|---------------|--------|-------------|
| Dauerlicht (DL) | an | an |
| Bereitschaftslicht (BL) | aus | an |
| Geschaltetes Dauerlicht | folgt dem Lichtschalter | an |
- **JOKER (1998):** Dauer- und Bereitschaftslicht im selben Stromkreis.
- **FUSION:** Schaltungsart **je Leuchte**, eingestellt am Steuerteil, ohne extra Datenleitung, auch dynamische Rettungszeichen am selben Kreis.

### Zwei Arten von Netzausfall
| Ausfall | Wer merkt es? | Reaktion | Strom kommt aus … |
|---------|---------------|----------|-------------------|
| **Hauptverteiler** (Einspeisung der Anlage) | die Anlage selbst | **Batteriebetrieb** | Batterie, 216 V DC |
| **Unterverteiler** der Allgemeinbeleuchtung | **DPÜ** in der Unterverteilung (Stromschleife/Bus) | Leuchten an, Anzeige „Netzausfall UV“ | **Netz** über die Anlage |

**Fail-safe:** Wird die Überwachungsschleife unterbrochen, geht das Licht **an**.

### Drei Versorgungskonzepte
| | Einzelbatterie (EB) | Gruppenbatterie (LPS) | Zentralbatterie (CPS) |
|---|---|---|---|
| Bild | jeder Fahrgast hat eine Powerbank | ein Akku pro Sitzreihe | ein großer Akku im Kofferraum |
| Leistung | je Leuchte | max. 1.500 W für 1 h bzw. 500 W für 3 h | unbegrenzt |
| Batterie-Lebensdauer | ≥ 4 Jahre | ≥ 5 Jahre | ≥ 10 Jahre (bei 20 °C) |
| Prüfen | jede Leuchte einzeln | zentral | zentral |

### Die 5 Bausteine (deine Landkarte)
```
 Netz 230/400 V AC
      │
 [1] Netzeinspeisung + Netzüberwachung ── DPÜ in den Unterverteilungen
      │
 [2] Ladeteil  ("Lichtmaschine": 80 % der Betriebsdauer in 12 h nachladen)
      │
 [3] Batterie  18 Blöcke × 12 V = 216 V DC, ortsfeste Bleibatterie, ≥ 10 Jahre
      │
 [4] Umschaltung + Endstromkreise (Stromkreismodule, max. 20 Leuchten/Kreis)
      │   Netzbetrieb: 230 V AC  →  Batteriebetrieb: 216 V DC
      ▼
   Leuchten (Betriebsgerät verträgt 220–240 V AC und 176–264 V DC)

 [5] Steuerung, Überwachung, Meldung: Touch-Steuerteil, Prüfbuch, Tests, Meldungen
```
- **Kein Wechselrichter nötig**, weil die Betriebsgeräte AC und DC vertragen. Deshalb heißen die Module bei INOTEC „Stromkreisumschaltungen“.
- **Auto-Analogie:** Ladeteil = Lichtmaschine · Steuerteil = Bordcomputer · Prüfbuch = Scheckheft · Funktionstest = Lampentest beim Zündung-An.
- ⚠️ **Keine Kfz-Starterbatterien.** 216 V DC sind **lebensgefährlich**. Am Batterieschrank nur mit Freigabe und gezogenen Batteriesicherungen arbeiten.
- **Transfer-Regel:** Vor jeder fremden Anlage die 5 Bausteine suchen.

## Selbsttest (Antworten unten)
1. Ersatzbeleuchtung vs. Sicherheitsbeleuchtung?
2. Mindest-Beleuchtungsstärke auf Rettungswegen, und ein Vergleich dazu?
3. Dauerlicht vs. Bereitschaftslicht?
4. Nur eine Unterverteilung fällt aus. Was passiert, und woher kommt der Strom?
5. Warum 216 V?
6. Warum kein Wechselrichter?
7. Die 5 Bausteine?
8. *(Bonus)* Warum brauchen Hotels bisher 8 h?

<details><summary>Antworten</summary>

1. Ersatz = weiterarbeiten. Sicherheit = Menschen sicher raus.
2. ≥ 1 lx auf dem Boden, etwa 4× Vollmond.
3. DL immer an. BL nur bei Ausfall der Allgemeinbeleuchtung.
4. Die DPÜ meldet, die Leuchten gehen an, versorgt mit Netzstrom über die Anlage. Anzeige „Netzausfall UV“.
5. 18 × 12-V-Blöcke in Reihe.
6. Die Betriebsgeräte vertragen AC und DC, die Anlage schaltet nur um.
7. Netzeinspeisung/-überwachung · Ladeteil · Batterie · Umschaltung/Endstromkreise · Steuerung/Überwachung/Meldung.
8. Die Gäste schlafen oder bleiben im Gebäude, nachts ist evtl. kein Personal da. Das Licht soll bis zum Morgen bzw. bis zur Behebung halten.
</details>

## Praxisauftrag (nur schauen, nichts öffnen ohne Kollegen)
- [ ] **Typenschild:** genaue Bezeichnung notieren, z. B. *CPS FUSION/11kW 1-ph* oder *CPS 220/64*.
- [ ] **Display:** Farbe des Statusfelds? Batteriespannung ablesen (Erwartung: eher um 240 V als genau 216 V; Auflösung in Folge 2).
- [ ] **Module:** Aufschriften der Einschübe (z. B. *CF 4x1A*) und die LEDs ansehen.
- [ ] **Batterieschrank** mit einem erfahrenen Kollegen ansehen: Wie viele Blöcke? (18, oder 36 bei zwei Strängen)
- [ ] *(Bonus)* Fragen, wo im Gebäude eine **DPÜ** sitzt.

**Ergebnisse gern zurückmelden.** Dann passe ich die nächsten Folgen an genau deine Anlage an.
