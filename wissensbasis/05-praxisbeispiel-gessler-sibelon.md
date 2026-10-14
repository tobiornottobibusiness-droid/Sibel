# Praxisbeispiel Transfer: Gessler SiBELON Kombischrank Lean (Fotos vom Nutzer, 14.10.2026)

> Quelle: Fotos des Nutzers von einer Anlage vor Ort (Kundenname bewusst weggelassen). Im Netz waren keine öffentlichen Herstellerunterlagen zu finden. Alles, was nicht auf Typenschild, Beschriftung oder Display steht, ist als **vermutlich** gekennzeichnet.
> Zweck: zeigen, dass sich die 5 Bausteine auch bei einem anderen Hersteller wiederfinden. Gut geeignet für Folge 13 (Transfer).

## Typenschild
- Gessler SiBELON Kombischrank Lean, Typ HVS: `HVS-L-3,3A-07kW-1UV` / `UVS1-20S-8I-1M`, Baujahr 2016
- Netz 400 V/3/N/PE, 50 Hz, bauseitige Absicherung 3 × 35 A
- **Batterie 216 V DC, 108 Zellen** (Typenschild: L12V15 108Z), **min. Versorgungsspannung 189 V DC nach 1 h** (= 1,75 V/Zelle)
- I Batt. 9,3 A / 1 h / 25 °C, Verbraucher 230 V, **P Verbr. 1.500 W**, IP20 / Schutzklasse I, Temperaturbereich +10 … +30 °C
- Normen auf dem Schild: EN 50171, EN 50172

## Zuordnung zu den 5 Bausteinen
| Baustein | Was auf den Fotos zu sehen ist |
|----------|--------------------------------|
| 1 Netzeinspeisung + Überwachung | Sicherung **-2F1 NETZ**. **Dreiphasen-Überwachungsrelais** K'Electric (U<sub>N</sub> 230/400 V AC, Ansprechwert U<sub>S</sub> = 85 % U<sub>N</sub>, t<sub>v</sub> = 0,5 s, 2 Wechsler, Testtaster). Das entspricht der INOTEC-DPÜ (dort ebenfalls 0,85 · U<sub>N</sub>) |
| 2 Ladeteil | Selbst nicht sichtbar. Sichtbar sind nur seine DC-Sicherungen **-2F10.1 / -2F10.2 „Ladung DC“**. Typbezeichnung „3,3A“ ist **vermutlich** der Ladestrom |
| 3 Batterie | Kombischrank mit 18 Blöcken **SSB SBL 18-12i** (12 V, 18 Ah, verschlossen), nummeriert 1–18, rote Polkappen, Lüftungsschlitze unten. Batteriesicherungen **-2F4 Batterie +** und **-2F5 Batterie −** (2-polig!). Hinweis: Das Typenschild nennt 15 Ah, verbaut sind 18-Ah-Blöcke, **vermutlich** ein Batterietausch |
| 4 Umschaltung + Endstromkreise | Anschlussraum mit **20 Endstromkreisen F1–F20**, jeweils rot/blau beschriftete Sicherungsklemmen, also **2-polig abgesichert** (Plus/L und Minus/N). Die Umschaltelemente sitzen **vermutlich** hinter den Abdeckungen bzw. in den Ausgangsmodulen der Steuerung |
| 5 Steuerung, Überwachung, Meldung | **SETLON-Steuerung**, eine Kleinsteuerung (SPS) mit E/A-Modulen 2A10, 2A11, 4A21, 4A31 … (Typ C750-8202, die Nummer deutet auf ein WAGO-750-System hin). LEDs: Betriebsstatus, Teststatus, Netz-/Ersatzbetrieb, Systemstörung intern, Dauerlicht, Systemstörung extern. **Touch-Display** in der Tür: Batteriespannung, Ladestrom, Batterietemperatur, Statusliste |
| Hilfsversorgung | **Mean Well DR-60-24** (24 V DC, 2,5 A = 60 W): Netzteil für die 24-V-Steuerkreise, **kein** Ladeteil |

## Schrankaufteilung (Gesamtfoto)
```
 Kabel von oben (orange Mantel = sehr wahrscheinlich Funktionserhaltkabel, Aufdruck prüfen)
┌────────────────────────────┬──────────────────────────┬──────────────────┐
│ Feld HVS (links)           │ Feld UVS1 (Mitte)        │ Feld rechts      │
│ oben: -2F11–13/-2F15       │ oben: 24-V-Netzteil      │ komplett         │
│  „Speisung vom Hauptnetz“, │  + Datenkabel            │ abgedeckt        │
│  Klemmleiste -2X1, 24-V-   │                          │ (Reserve oder    │
│  Klemmen S2–S7, Netzteil,  │ Mitte: F1–F20            │  Ladeteil →      │
│  Dreiphasenwächter         │  Endstromkreise 2-polig  │  Schaltplan)     │
│ Mitte: -2F4/-2F5 Batterie, │ dahinter vermutlich      │                  │
│  -2F1 Netz, -2F10.x Ladung │  Umschaltrelais          │                  │
│ unten: Fenster Steuerung   │                          │                  │
├────────────────────────────┴──────────────────────────┴──────────────────┤
│ Batteriefach: 18 Blöcke auf drei Etagen, Lüftungsschlitze unten          │
└──────────────────────────────────────────────────────────────────────────┘
 Tür: Touch-Display außen, Dokumententasche innen, grün-gelbe Türerdung
```
- Die LED-Legende an der linken Innenwand nennt „PFC“ und „K-Bus“. Das sind Begriffe aus dem WAGO-750-System, die Steuerung ist also eine WAGO-PFC-SPS.
- Das Ladeteil ist auf den Fotos nicht zu sehen. Dass es da ist, zeigen der Ladestrom auf dem Display und die Sicherungen „Ladung DC“. **Vermutlich** sitzt es hinter den Berührungsschutz-Abdeckungen (HVS-Feld oder rechtes Feld). Wo genau, zeigt der Schaltplan.

## Ablesewerte am Display (Momentaufnahme)
- 245,10 V ÷ 108 = **2,27 V/Zelle**, also Erhaltungsladung wie im Lehrbuch (Folge 2)
- Batterietemperatur 20,6 °C (ideal 20 °C)
- Ladestrom 1,10 A: für eine volle 18-Ah-Batterie in Erhaltungsladung eher hoch. Mögliche Gründe: Nachladen nach einem Test, oder die Anzeige enthält den Eigenverbrauch. **Klären**
- Status: betriebsbereit, Netzbetrieb, Dauerlicht ein, **Leuchtenstörung aktiv** (auch die rote LED „Systemstörung extern“ an der Steuerung leuchtet)

## Lernpunkte
- Sicherungen sind **Schutz- und Trennstellen**, keine Überwachung. Die Überwachung macht der Phasenwächter.
- Die Batterie ist **2-polig abgesichert**, die Endstromkreise ebenfalls. Das ist die DC-Regel aus Folge 2 in echt.
- „min. Versorgungsspannung 189 V nach 1 h“ = 1,75 V/Zelle. Bei kurzen Entladungen (1 h) darf die Entladeschlussspannung tiefer liegen als bei langen (1,8 V/Zelle bei > 3 h; Zumtobel-Batteriemerkblatt). Das erklärt auch INOTEC CPS 220/64 mit 194 V und FUSION mit 185 V.
- 1.500 W für 1 h ist genau die Leistungsgrenze, die EN 50171 für LPS nennt. Ob diese Anlage als LPS oder CPS eingestuft ist, steht in den Herstellerunterlagen.
