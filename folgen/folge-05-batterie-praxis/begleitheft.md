# Begleitheft Folge 5 – Die Batterie in der Praxis

**Audio:** [folge-05-batterie-praxis.mp3](folge-05-batterie-praxis.mp3) · **Kapitelmarken:** [kapitel.txt](kapitel.txt) · **Wörtliches Skript:** [skript.md](skript.md)
**Ausführlich:** [wissensbasis/01-cps-fusion-anlage.md](../../wissensbasis/01-cps-fusion-anlage.md) (Abschnitt 6 und 6.6) · Lernmaterial, ersetzt weder Herstelleranleitung noch Betriebsanweisung

## Lernziele
Nach dieser Folge kannst du …
1. verschlossene und geschlossene Batterien unterscheiden und weißt, was das für die Wartung heißt.
2. Alterung, 25 % Reserve und den Einfluss der Temperatur erklären.
3. die Ursachen einer Tiefentladung nennen und weißt, wie der Tiefentladeschutz arbeitet.
4. erklären, warum es eine Einzelblocküberwachung (BCS) gibt.
5. eine Batterieinspektion durchführen und protokollieren und kennst den Ablauf beim Batterietausch.
6. die Anforderungen an den Aufstellraum (Wasserstoff, Lüftung, Boden, Zugang) einordnen.

## ⚠️ Sicherheit zuerst
**216 V DC, die Batterie lässt sich nicht abschalten, die Pole stehen immer unter Spannung.** Arbeit nur nach Betriebsanweisung und Anleitung von Anlagen- und Batteriehersteller. Schutzbrille, Schutzkleidung, isoliertes Werkzeug, Schmuck ab, nie Werkzeug oder Gegenstände auf die Batterie legen. Kein Feuer, keine Funken. Säure im Auge oder auf der Haut: sofort mit viel Wasser spülen, dann zum Arzt.

## Spickzettel

### Bauarten
| | Verschlossen (Standard in CPS) | Geschlossen |
|---|---|---|
| Beispiele | **OGi**-Blöcke 12 V (Vlies/AGM), **OPzV** (Panzerplatte, Gel) | **OPzS** (2-V-Zellen, Panzerplatte, flüssige Säure, DIN 40736) |
| Wasser nachfüllen | **verboten**, Ventile nicht öffnen | **ja**, destilliertes/gereinigtes Wasser |
| Säuredichte messen | nein | ja, Sollwert vom Hersteller (z. B. 1,24 ± 0,01 kg/l bei 20 °C) |
| Lüftung | gering | deutlich mehr |
| Boden | tragfähig, ableitfähig | zusätzlich säurebeständig oder Auffangwanne |
| Schilder (Schrank) | – | innen: säurehaltig + Erste Hilfe; außen: Explosionsgefahr, keine offenen Flammen |

- Nur **ortsfeste Bleibatterien** (EN 60896-11/-21/-22), **≥ 10 Jahre bei 20 °C**. **Keine Kfz-Starterbatterien** (Sprinter statt Marathonläufer).
- CPS 220/64: 18 Blöcke × 12 V = 216 V (108 Zellen).

### Alterung und Temperatur
| Thema | Wert |
|---|---|
| Kapazitätsverlust | bis 2,5 %/Jahr (≈ 25 % in 10 Jahren) |
| Alterungsreserve (EN 50171) | **25 %**. Katalogbeispiel: 21,2 A + 25 % = 26,5 A für 3 h |
| Lebensende (Praxis) | Betriebsdauertest schafft die geforderte Zeit nicht mehr |
| Ideal | **20 °C** (± 5 °C) |
| Faustregel | **+10 °C ≈ halbe Lebensdauer** (15 Jahre bei 20 °C → 7,5 Jahre bei 30 °C) |
| Grenzen | dauerhaft > 45 °C vermeiden, 55 °C Grenze |
| Blöcke untereinander | Unterschied < 3 °C anstreben (Abstand ≥ 0,5 cm); > 5 °C → Kundendienst |
| Temperaturkompensation | **Quellen unterscheiden sich:** −3 mV/Zelle/K (Zumtobel) bzw. −5 mV/Zelle/°C außerhalb 15–25 °C (Banner). Batteriehersteller entscheidet. INOTEC: Fühler an T+/T− des RIF 5 oder BCS |

### Tiefentladung
- Entladen bildet **Bleisulfat**. Bleibt die Batterie leer stehen, verhärtet es (**Sulfatierung**), Kapazität dauerhaft weg.
- **Tiefentladeschutz** trennt die Verbraucher. Testwert CPS 220/64 **194 V**, FUSION **185 V**. Nach Auslösung **quittieren**, Ursache klären, laden, Kapazität prüfen.

| Entladedauer | Entladeschlussspannung (Richtwert Zumtobel) | Beispiel |
|---|---|---|
| > 3 h | 1,80 V/Zelle | 194 V ÷ 108 ≈ 1,80 (CPS 220/64) |
| 1–3 h | 1,75 V/Zelle | Gessler: 189 V nach 1 h ÷ 108 = 1,75 |
| 20 min–1 h | 1,67 V/Zelle | |
| < 20 min | 1,60 V/Zelle | |

**Typische Ursachen:** langer Netzausfall bei nicht blockiertem Notlicht · abgeschaltete Anlage mit angeschlossener Batterie (Eigenverbrauch + Selbstentladung → **bei längerer Netzunterbrechung Batteriesicherungen ziehen**) · keine Wiederaufladung nach Entladung (Ladeteil gestört).
**Regeln:** nach jeder Entladung sofort laden, spätestens nach 24 h · max. 3 Monate ohne Ladung lagern · entladene Batterien können einfrieren.

### BCS – Einzelblocküberwachung
- 18 Blöcke in Reihe = **Kette**: ein schwaches Glied reicht. Der kurze Funktionstest findet es oft nicht; Mittelabgriff vergleicht nur 2 × 9 Blöcke.
- Typische Fehler: Austrocknen, thermisches Durchgehen, Plattenschluss, „Sudden Death“ (korrodierte Polverbindung reißt ab).
- BCS: bis 36 Sensoren am 2-Draht-Bus, Blockspannung + -temperatur, etwa alle 40 s. Grenzwerte: **≤ 10,3 V**, **> 15,0 V**, Temperatur > 50 / 80 / 85 °C.
- Reaktion: Netzbetrieb → **Ladung aus**; Betriebsdauertest → **Abbruch**. Wieder ein nur von Hand (Menü „Ladung einschalten“) mit Prüfbucheintrag.
- EN 50171:2022: Überwachung muss Einzelblockspannungen ermitteln und auswerten können, Einzelblockprüfung beim wöchentlichen FT empfohlen.

### Inspektion und Protokoll
| Wann | Was |
|---|---|
| **alle 6 Monate** | Sichtprüfung (Risse, aufgebläht, Säurespuren, Korrosion, Polkappen, lose/verfärbte Verbinder, Staub), Erhaltungsladespannung **gesamt und je Block**, Oberflächentemperatur der Blöcke, Raumtemperatur |
| **mind. alle 12 Monate** | zusätzlich alle Verbindungen mit **Drehmomentschlüssel** nachziehen (Wert vom Batteriehersteller, z. B. M5 5 Nm, M6 7 Nm, M8 10 Nm), **Blockspannungen während des Betriebsdauertests** aufzeichnen |

- Sollwert 12-V-Block bei 2,27 V/Zelle ≈ **13,6 V**; Bereich ältere Batterie 13,32–13,80 V (erste 6 Monate 13,20–13,92 V).
- **Protokoll = Garantiegrundlage** (z. B. zwei letzte Wartungsberichte für eine Reklamation). Mindestinhalt: Raumtemperatur, Ladespannung/-strom, Entladestrom, Block- und Gesamtspannungen am Anfang und Ende der Belastung.
- Messen unter Spannung: Schutzbrille, isolierte Prüfspitzen, nie zwei Pole überbrücken. Zwischen erstem und letztem Block ≈ **245 V DC**.
- Reinigen nur mit Wasser ohne Zusatz (Kriechströme vermeiden).

### Batterietausch (INOTEC)
1. Lieferung auf Vollständigkeit und Schäden prüfen; Ruhespannung 12-V-Block **≥ 12,60 V**, sonst nachladen.
2. **Anlage blockieren → Batteriesicherungen ziehen.**
3. Isoliertes Werkzeug, Drehmoment des Batterieherstellers, Blöcke **polrichtig** verschalten, **Schutzkappen** auf die Pole, bei BCS Adapter unter die Polverbinder.
4. Erst nach Abschluss Batteriesicherungen einsetzen (Polung prüfen).
5. Vor der ersten Funktionsprüfung **mind. 24 h laden**. Volle Kapazität erst nach **4–5 Wochen** Erhaltungsladung → Betriebsdauertest nicht am Tag nach dem Tausch.
6. Altbatterien ins Recycling, **Dokumentation und Typenschild nachführen**.

### Aufstellraum
| Anforderung | Wert / Regel |
|---|---|
| Schutzziel | H₂ **< 4 Vol.-%** → Raum gilt nicht als explosionsgefährdet |
| Luftstrom (EN IEC 62485-2) | Q = 0,05 · n · I<sub>gas</sub> · C<sub>N</sub> · 10⁻³ m³/h; I<sub>gas</sub> = 1 (Erhaltung, Sicherheitsbeleuchtung) bzw. 8 (Starkladung) |
| Beispiel 216 V/70 Ah, verschlossen | Q = 0,378 m³/h; dichte Rauchschutztür: bis 9 m³/h Leckrate (23-fach) |
| Öffnungen 216 V/100 Ah | verschlossen ≈ **16 cm²** je Zu-/Abluft; geschlossen **≥ 76 cm²**; A = 28 · Q |
| Lage der Öffnungen | Wasserstoff steigt nach oben → Abluft in der Regel oben, Zuluft unten/gegenüber |
| Baurecht (Muster-EltBauVO) | verschlossen ≤ 20 kWh (≈ 216 V/92 Ah): bei ausreichender natürlicher Lüftung keine Lüftung ins Freie nötig |
| Boden | tragfähig; geschlossen: säurebeständig oder Auffangwanne; Armreichweite ableitfähig < 10 MΩ (oder Gummimatte) |
| Zugang / Tür | > 120 V DC nur Befugte (verschlossen/verriegelt); Tür nach außen, Panikfunktion |

### Transfer-Ecke
| | Gessler SiBELON | Kaufel viaFlex |
|---|---|---|
| Batterie | 18 × 12 V, 18 Ah, **verschlossen** (SSB SBL 18-12i), nummeriert, rote Polkappen | **108 × 2 V OPzS 1200 Ah, geschlossen**, Gestell im eigenen Raum |
| Ablesung | 245,10 V ÷ 108 = **2,27 V/Zelle**, 20,6 °C | max. 259,2 V ÷ 108 = 2,4 V/Zelle (Starkladung) |
| Absicherung | 2-polig: -2F4 / -2F5 | -F111 (+) / -F112 (−) |
| Besonderheiten | Typenschild nennt noch 15 Ah (Doku nicht nachgeführt) | Wasser nachfüllen, Säuredichte, säurefester Boden/Wanne, Lüftung (allein wegen Kapazität ≈ 17-fach gegenüber 70 Ah, dazu höhere Gasung) |

**Fragen für deinen nächsten Kaufel-Besuch:** Auffangwanne oder säurefester Boden? Wo sind die Lüftungsöffnungen? Hängen die Warnschilder? Wann wurde laut Protokoll zuletzt Wasser nachgefüllt?

## Selbsttest
1. Unterschied verschlossene und geschlossene Batterie?
2. Warum 25 % Reserve?
3. Was passiert mit der Lebensdauer bei dauerhaft 30 °C statt 20 °C?
4. Zwei typische Ursachen für eine Tiefentladung?
5. Warum findet der wöchentliche Funktionstest einen schlechten Block oft nicht?
6. Was gehört mindestens jährlich zur Batterieinspektion?
7. Welches Schutzziel gilt für den Aufstellraum?
8. *(Bonus)* Warum darf der Tiefentladeschutz bei einer 1-h-Anlage tiefer liegen als bei einer 3-h-Anlage?

<details><summary>Antworten</summary>

1. Verschlossen: Säure im Vlies/Gel, kein Wasser nachfüllen, Ventile zu. Geschlossen: flüssige Säure, Wasser nachfüllen, Säuredichte messen, mehr Lüftung, säurefester Boden.
2. Kapazitätsverlust bis 2,5 %/Jahr; auch am Ende der Gebrauchsdauer muss die volle Nennbetriebsdauer erreicht werden (EN 50171).
3. Faustregel: ungefähr halbiert.
4. Langer Netzausfall bei nicht blockiertem Notlicht; abgeschaltete Anlage mit angeschlossener Batterie; keine Wiederaufladung nach Entladung.
5. Der Test ist kurz, die übrigen Blöcke liefern genug Energie. Erst bei langer Entladung bricht die Spannung ein → Einzelblocküberwachung (BCS).
6. Verbindungen mit Drehmomentschlüssel nachziehen, Blockspannungen beim Betriebsdauertest aufzeichnen (plus die halbjährlichen Punkte). Protokoll = Garantiegrundlage.
7. Wasserstoff < 4 Vol.-%.
8. Bei hohem Entladestrom bricht die Spannung wegen des Innenwiderstands stärker ein, ohne dass die Batterie tiefer entladen ist. Richtwerte: > 3 h 1,80 V/Zelle, 1–3 h 1,75 V/Zelle.
</details>

## Praxisauftrag
- [ ] **Batterie ansehen:** verschlossen oder geschlossen? Wie viele Blöcke/Zellen, Einbaujahr, passt es zum Typenschild?
- [ ] **Spannung pro Zelle:** Batteriespannung und Temperatur am Display ablesen, durch die Zellenzahl teilen.
- [ ] **Batterieprotokoll** im Prüfbuch oder in der Dokumententasche suchen: Stehen die Blockspannungen vom letzten Betriebsdauertest drin?

**Nächste Folge:** Netz, Laden, Umschalten – Ladeteil, Netzüberwachung (RIF 5, DPÜ, Stromschleife), Nachlauf, Handrückschaltung, Blockieren und die **24-V-Hilfsversorgung**.
