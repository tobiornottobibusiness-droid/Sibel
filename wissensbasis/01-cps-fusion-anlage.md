# Wissensbasis: INOTEC CPS FUSION (Zentralbatteriesystem)

> Stand der Recherche: Oktober 2026.
> Hauptquellen: INOTEC Montage- und Betriebsanleitung CPS FUSION (MAN 708243, TFT-Touch-Steuerteil, Softwarestand V3.5.10/2.6.0), INOTEC Katalog CPS FUSION 02/2023 (CAT 707126), INOTEC Handbuch Sicherheitsbeleuchtung 2025. Vollständige Liste: [quellen.md](quellen.md).
>
> **Hinweis zur Typbezeichnung „FUSION 64“:** INOTEC führt keine Anlage mit dem Namen „CPS FUSION 64“. Es gibt:
> - die **CPS FUSION** (aktuelle Generation, Typen nach Leistung: 1,5 kW / 5,5 kW / 11 kW / 22 kW) und
> - die Vorgängergeneration **CPS 220/64** (seit 2007 mit TFT-Display, Stromkreismodule „CP …“).
>
> Die „64“ kann außerdem von der CPS FUSION/5,5 kW stammen: Sie hat 16 externe Modulplätze für bis zu **64 zusätzliche Stromkreise**. Was genau verbaut ist, steht auf dem **Typenschild**. Die Grundprinzipien sind in beiden Generationen gleich. Die Unterschiede stehen in Abschnitt 11.

---

## 0. Das Denkmodell: 5 Bausteine jeder Zentralbatterieanlage

Jede Zentralbatterieanlage (CPS) besteht aus denselben fünf Funktionsblöcken, egal von welchem Hersteller. Wer diese fünf Blöcke in einer Anlage wiederfindet, versteht jede Anlage.

| # | Baustein | Aufgabe | Bei der CPS FUSION |
|---|----------|---------|--------------------|
| 1 | **Netzeinspeisung & Netzüberwachung** | Strom aus dem Hauptverteiler holen; erkennen, wann das Netz weg ist | Klemmleiste X1, Netzsicherung 1F1, RIF 5 überwacht den Hauptverteiler, DPÜ/DPÜ/B überwachen die Unterverteiler |
| 2 | **Ladeteil** | Batterie laden und voll halten | Ladeteile LT 1,2 A / 3 A / 7 A (216 V) |
| 3 | **Batterie** | Energiespeicher für den Notfall | 18 verschlossene Blei-Blockbatterien à 12 V in Reihe = **216 V DC**; optional BCS-Überwachung jedes Blocks |
| 4 | **Umschaltung & Endstromkreise** | Leuchtenstromkreise von Netz auf Batterie umschalten, absichern, überwachen | Stromkreismodule (Einschübe) CF 4x1A, CF 2x2,5A, CF 1x5A, CP 2x2,5A/24V; Klemmleiste X3 |
| 5 | **Steuerung, Überwachung, Meldung** | Testen, protokollieren, anzeigen, melden | 5"-TFT-Touch-Steuerteil in der Tür, Prüfbuch, RIF 5-Meldekontakte, INOWeb, Busse IB1/IB2/IB3, RTG |

Dazu kommen außerhalb des Schranks: **Leitungsanlage** (oft mit Funktionserhalt E30), **Leuchten mit Betriebsgeräten** und **Erweiterungen** (Unterstationen, Schaltmodule, Meldetableau).

---

## 1. Was ist die CPS FUSION?

- **Hersteller:** INOTEC Sicherheitstechnik GmbH, Ense (Westfalen), gegründet 1995.
- **Gerätetyp:** Zentralbatteriesystem (CPS = *Central Power Supply System*) nach **DIN EN 50171**. Laut Handbuch ist es ein „batteriegestütztes Überwachungs- und Versorgungsgerät für den Notlichtbetrieb von Sicherheits- und Rettungszeichenleuchten sowie bodennahen Leitsystemen“.
- **Name:** „FUSION“ heißt Verschmelzung. INOTEC verbindet hier zentrale und dezentrale Konzepte und Techniken.
- **Kernidee „FUSION-Technik“:** Dauerlicht, Bereitschaftslicht, geschaltetes Dauerlicht, gedimmte und **dynamische** Leuchten können **im selben Stromkreis** laufen. Dafür braucht es **keine zusätzliche Datenleitung**: Die Kommunikation läuft über die normale Versorgungsleitung (L, N, PE).
- **Vorgeschichte:** 1998 stellte INOTEC den Mischbetrieb von Dauer- und Bereitschaftslicht in einem Stromkreis vor, unter dem Namen **„JOKER“**. Bei JOKER wird die Schaltungsart am Modul in der Leuchte eingestellt. Bei FUSION geschieht das am Steuerteil oder in der Konfigurator-Software.

---

## 2. Ausbaustufen (Gerätetypen)

| Typ | Max. Anschlussleistung | Netz | Modulplätze intern/extern | Max. Stromkreise | Ladeteil | Max. Batterie im Schrank | Schrank H×B×T (mm) |
|-----|-----|-----|-----|-----|-----|-----|-----|
| CPS FUSION/1,5kW/1,2A | 1,5 kW | 1~ 230 V | 5 / – | 20 | 1,2 A | 28 Ah | 1600×600×330 |
| CPS FUSION/1,5kW/3A | 1,5 kW | 1~ 230 V | 5 / – | 20 | 3 A | 28 Ah | 1800×600×330 |
| CPS FUSION/5,5kW/3A | 5,5 kW | 1~ 230 V | 5 / 16 | 20 + 64 | 3 A | 28 Ah | 1800×600×330 |
| CPS FUSION/5,5kW 1-ph | 5,5 kW | 1~ 230 V | 5 / 16 | 20 + 64 | 3 A oder 7 A | 75 Ah | 2030×800×400 |
| CPS FUSION/11kW 1-ph | 11 kW | 1~ 230 V | 16 / 16 | 128 | 2× 3 A oder 7 A | 75 Ah | 2030×800×400 |
| CPS FUSION/11kW 3-ph | 11 kW | 3~ 400 V | 16 / 16 | 128 | 2× 3 A oder 7 A | 75 Ah | 2230×800×400 |
| CPS FUSION/11kW 3-ph 2m | 11 kW | 3~ 400 V | 16 / 16 | 128 | bis 6× 3 A oder 7 A | separat | 2030×800×400 |
| CPS FUSION/22kW 3-ph 2m | 22 kW | 3~ 400 V | 16 / 16 | 128 | bis 6× 3 A oder 7 A | separat | 2030×800×400 |
| CPUS FUSION/11kW 1-ph (Unterstation) | 11 kW | 1~ 230 V | 16 / 16 | 128 | **keins** | – | 830×800×400 |

Allgemeine Gerätedaten: Schutzklasse I, Schutzart IP20, Umgebungstemperatur −5 °C bis +35 °C, max. 85 % relative Luftfeuchte (nicht kondensierend), Batterie **216 V DC**, Farbe RAL 7035 (lichtgrau). Optional mit Brandschutzgehäuse BRS (Funktionserhalt 30 min, abZ Z-86.1-95).

**Maximalausbau eines Steuerteils:** 128 Stromkreise × 20 Leuchten = **2.560 Leuchten**.

---

## 3. Aufbau des Schranks (von außen nach innen)

- **Elektronikschrank** (oben) und **Batterieschrank** (unten oder daneben) werden aufeinandergesetzt und verschraubt. Mit Wandlaschen wird der nötige Wandabstand eingehalten.
- **Tür:** Hier sitzt das **5"-TFT-Touch-Steuerteil** mit USB-Anschluss und Reset-Taster. Man kann die Anlage bedienen, ohne die Tür zu öffnen.
- **Baugruppenträger** (19"): Steckplätze für die Stromkreismodule (Einschübe). Bei Auslieferung klebt eine Schutzabdeckung auf dem obersten Baugruppenträger (gegen Verdrahtungsreste). Sie muss vor dem Einschalten entfernt werden.
- **Ladeteil(e):** Einschübe „Charger 216V/7A“ o. ä. mit eigener AC-Sicherung (16 AT) und DC-Sicherung (10 AT) sowie Schalter.
- **Klemmen-/Anschlussraum:** Kabeleinführung über die ganze Schrankbreite (Schiebeblech mit verschiebbarer Gummidichtung) oder Verschraubungen (M20/M25/M32/M50).
- **Batteriesicherungen F1/F2:** Trennen die Batterie vom Gerät. Sie werden bei Montage und Abschaltung gezogen.
- **Klemmleisten:**
  - **X1** – Netzanschluss (L über Sicherung 1F1, N, PE)
  - **X2** – Busse und Daten: IB2, IB3, RTG, +24 V, ⊥
  - **X3** – Endstromkreise 230 V (L, N, PE je Stromkreis; Trennklemmen für die Isolationsmessung)
  - **X5/X7** – Endstromkreise der 24-V-Module
  - **X8** – weitere Baugruppen (RIF 5, LSA 8.1, DPÜ)

---

## 4. Baustein 1: Netzeinspeisung und Netzüberwachung

### 4.1 Netzanschluss
- 1-phasig 230 V AC ±10 % oder 3-phasig 400 V AC ±10 %, 50/60 Hz.
- Systemstrom intern z. B. 50 A (11 kW) bzw. 63 A intern / 100 A gesamt (22 kW).
- Stromaufnahme der Ladeteile: 7-A-Lader ≈ 9 A, 3-A-Lader ≈ 4 A, 1,2-A-Lader ≈ 2 A (Netzseite). Laut Katalogtabelle braucht ein LT 216V/7A 9,1 A bzw. 2.100 VA.
- Bei 3-phasiger Einspeisung ist eine **Dreiphasenüberwachung (DPÜ)** im Gerät eingebaut.

### 4.2 Zwei Arten von Netzausfall – das wichtigste Konzept

| Ereignis | Erkannt durch | Reaktion der Anlage | Woher kommt der Strom für die Leuchten? |
|----------|---------------|---------------------|-----------------------------------------|
| **Netzausfall Hauptverteiler** (HV, Einspeisung der CPS selbst) | RIF 5 (Klemmen L/N, werkseitig verdrahtet) | **Batteriebetrieb**: alle Verbraucher schalten auf die Batterie | Batterie (216 V DC) |
| **Netzausfall Unterverteiler** („Netzausfall UV“) der Allgemeinbeleuchtung | DPÜ in der Unterverteilung (über die 24-V-Stromschleife) oder DPÜ/B (über den Bus) | Leuchten werden eingeschaltet, je nach Programmierung alle oder selektiv | **Netz** über die CPS, solange die CPS selbst Netz hat |

Merksatz aus dem Handbuch: *Die eingestellte Schaltungsart ist nur im Netzbetrieb aktiv. Bei Netzausfall UV werden alle Verbraucher eingeschaltet, mit Netzspannung aus der CPS. Bei Netzausfall am Hauptverteiler der Sicherheitsbeleuchtung werden alle Verbraucher in Batteriebetrieb geschaltet.*

### 4.3 Dreiphasenüberwachungen
- **DPÜ** (ohne Bus): sitzt in der Unterverteilung der Allgemeinbeleuchtung (UVA). Wenn eine Phase ausfällt (Ansprechwert 0,85 × U<sub>N</sub>), öffnet sie ihren Kontakt und unterbricht die **24-V-Stromschleife (SL+/SL−)** am RIF 5. Mehrere DPÜ werden **in Reihe** geschaltet. Werkseitig sind SL+/SL− gebrückt. Meldung im Steuerteil: „Netzausfall UV“.
- **DPÜ/B.2** (mit Bus): meldet die **Adresse und die ausgefallene Phase** über den Bus (IB2 oder IB3, nicht gemischt; Adressen 1…31). Nachlaufzeit nach Netzwiederkehr einstellbar: 0/5/10/15 min. Damit ist ein **selektiver** Notlichtnachlauf möglich. Fällt der Bus aus, schalten die zugeordneten Bereitschaftsleuchten ein.
- **Schleifenüberwachung (SLÜ):** Mit einer **Zener-Abschlussdiode** am letzten DPÜ erkennt die Anlage nicht nur Unterbrechung, sondern auch Kurzschluss der Schleife. LOMO-Modul: Loop-Monitoring je Strang.
- **Fail-safe-Prinzip:** Eine Unterbrechung (Draht ab, DPÜ defekt) schaltet das Licht EIN, nicht aus.

### 4.4 Fernschalter und Blockieren
- Eingang **FS+/FS−** am RIF 5: Damit lässt sich über einen externen Schalter (oder den Schlüsselschalter am MTB) **Dauerlicht** oder **Dauer- und Notlicht** blockieren (je nach Programmierung).
- **Achtung:** Bei „Dauer- und Notlicht blockiert“ bleibt das Notlicht bei Netzausfall **aus**. Das ist sinnvoll außerhalb der Nutzungszeiten (verhindert Tiefentladung), aber gefährlich, wenn man es vergisst.
- Eine Blockierung über Fernschalter oder Fernüberwachung kann nur dort auch wieder freigegeben werden.

---

## 5. Baustein 2: Ladeteil

- Ladeteile: **LT 220V/1,2A**, **LT 216V/3A**, **LT 216V/7A**. Große Geräte können mehrere Ladeteile haben (bis 4 im Schrank bzw. 6 × 3 A/7 A beim 2-m-Schrank).
- **Anforderung DIN EN 50171:** Eine entladene Batterie muss nach **12 Stunden** wieder **80 %** ihrer festgelegten Betriebsdauer liefern können. Für die Ladestromberechnung zählt die Alterungsreserve nicht mit.
- **Temperaturgeführte Ladung:** Ein Temperaturfühler (KTY oder INOTEC-Sensor) im Batterieraum wird an T+/T− des RIF 5 angeschlossen und im Steuerteil aktiviert. Mit BCS übernehmen die Blocksensoren diese Aufgabe.
- **Lüftersteuerung:** Ein RIF-5-Kontakt schaltet jede Stunde zu einer einstellbaren Minute für eine einstellbare Dauer einen externen Lüfter. Bei **Starkladung** wird er immer eingeschaltet.
- Begriffe: **Erhaltungsladung** (Batterie voll halten, kleiner Strom) und **Starkladung** (nach Entladung schnell nachladen). Bei Starkladung gast eine Bleibatterie mehr; das wird bei der Lüftungsberechnung berücksichtigt.

---

## 6. Baustein 3: Batterie

### 6.1 Grunddaten
- **Nur ortsfeste Bleibatterien** sind zulässig (EN 60896-11, -21, -22). Andere Batteriearten sind bei der CPS FUSION nicht vorgesehen. **Keine Kfz-Starterbatterien.**
- Standard: **verschlossene OGi-Blockbatterie**, **18 Blöcke à 12 V in Reihe = 216 V DC** (= 108 Zellen à 2 V).
- **Gebrauchsdauer mindestens 10 Jahre bei 20 °C** (Anforderung DIN EN 50171).
- **Tiefentladeschutz:** Er trennt die Verbraucher von der Batterie, wenn die Spannung zu tief fällt. Beim Test wird bis **185 V** heruntergefahren (≈ 1,71 V je Zelle). Nach einer Auslösung muss man ihn am Steuerteil **quittieren**.
- Bei geschlossenen (nicht verschlossenen) Batterien braucht es Warnschilder (Elektrolyt, Explosionsgefahr).
- **Lebensgefahr:** 216 V DC. Vor Arbeiten die Batteriesicherungen F1/F2 ziehen und auf richtige Polung achten.

### 6.2 Batterietypen im Katalog (Auszug)
Bezeichnung „20-xx“. Kapazitätsangabe C10 bis 1,8 V/Zelle. Entladeströme ohne Alterungszuschlag:

| Typ | 1 h | 3 h | 8 h | Gewicht gesamt | Schrank |
|-----|-----|-----|-----|-----|-----|
| 20-12 | 6,3 A | 3,0 A | 1,3 A | 72 kg | 1000×600×330 |
| 20-28 | 16,2 A | 6,8 A | 2,9 A | 171 kg | 1000×600×330 |
| 20-55 | 33,3 A | 13,8 A | 6,4 A | 405 kg | 1200×800×400 |
| 20-90 | 66,8 A | 25,8 A | 11,1 A | 590 kg | 2× 1200×800×400 |
| 20-230 | 142 A | 64,2 A | 27,0 A | 1.323 kg | 6× 1200×800×400 |

### 6.3 Alterung und Dimensionierung
- Bleibatterien verlieren im Normalbetrieb bis zu **2,5 % Kapazität pro Jahr** (25 % in 10 Jahren).
- **DIN EN 50171:** **25 % Alterungsreserve** einplanen. Basis: 80 % entnehmbare Kapazität am Ende der Gebrauchsdauer bei 20 °C. Bei höheren Temperaturen braucht es mehr Reserve: bei 30 °C für verschlossene Batterien ≥ 81,8 %. Deshalb gilt: **Batterieraum auf 20 °C halten.**
- **Lebensende** ist erreicht, wenn am Ende der Nennbetriebsdauer die Batteriespannung bei Nennlast unter 90 % der Nennspannung fällt. In der Praxis heißt das: Die Batterie wird getauscht, wenn sie im jährlichen Betriebsdauertest die geforderte Zeit nicht mehr schafft.
- **Rechenbeispiel aus dem Katalog:** Versammlungsstätte, 3 h. Summe der Leuchtenströme 21,2 A, plus 25 % → 26,5 A. Gewählt wird Batterie 20-90. Laden: 1 Ladeteil 7 A. Netzanschluss: 5,81 kVA Leuchten + 2,10 kVA Ladeteil = 7,91 kVA.

### 6.4 BCS – Battery Control System (optional)
- Problem: Alle 18 Blöcke sind in Reihe geschaltet. **Ein defekter Block kann die ganze Batterie unbrauchbar machen.** Den kurzen wöchentlichen Funktionstest besteht die Batterie trotzdem, weil die übrigen Blöcke genug Energie dafür haben. Die übliche Überwachung über einen **Mittelabgriff** vergleicht nur zwei Hälften à 9 Blöcke.
- Typische Batteriefehler: Austrocknen (Elektrolyt in Vlies/Gel), thermisches Durchgehen (*thermal runaway*), Plattenschluss, „Sudden Death“ (korrodierte Polverbindung reißt ab).
- **BCS:** bis zu **36 Sensoren** (einer je Block) an einem 2-adrigen Bus und ein BCS-Modul. Gemessen werden **Blockspannung und Blocktemperatur**. Abfrage etwa alle 40 s.
- **Grenzwerte am Sensor:** Unterspannung ≤ 10,3 V, Überspannung > 15,0 V, Temperatur > 50 °C / > 80 °C / > 85 °C.
- **Reaktion:** Im Netzbetrieb bei Unterspannung oder Übertemperatur: **Ladung aus**. Im Betriebsdauertest bei Unterspannung: **Test wird abgebrochen**. Wieder einschalten geht nur manuell mit Prüfbucheintrag.
- DIN EN 50171:2022 verlangt, dass Batterieüberwachungssysteme die **Einzelblockspannungen** ermitteln und auswerten können, und empfiehlt eine Einzelblockprüfung beim wöchentlichen Funktionstest.

### 6.5 Unterbringung und Lüftung
- Bleibatterien gasen Wasserstoff aus. Schutzziel: **Wasserstoffkonzentration < 4 Vol.-%**.
- Formel nach DIN EN IEC 62485-2: Q = 0,05 · n · I<sub>gas</sub> · C<sub>N</sub> · 10⁻³ m³/h, Lüftungsquerschnitt A = 28 · Q (cm²). Für eine CPS-Batterie 216 V/70 Ah ist Q ≈ 0,38 m³/h. Die Undichtigkeiten normaler Türen reichen dafür meist schon aus.
- **Muster-EltBauVO:** Verschlossene Batterien bis **2 kWh** (≈ 216 V/9,2 Ah) sind vom Anwendungsbereich ausgenommen. Bis **20 kWh** (≈ 216 V/92 Ah) kann man bei ausreichender natürlicher Lüftung auf eine Lüftung ins Freie verzichten.
- Batteriespannung über 120 V DC: Der Zugang muss durch Verriegelung o. ä. eingeschränkt sein.

---

## 7. Baustein 4: Umschaltung und Endstromkreise

### 7.1 Warum 216 V Gleichspannung? Und was „Umschaltung“ heißt
- Im **Netzbetrieb** bekommen die Leuchtenstromkreise **230 V Wechselspannung** (über die CPS).
- Im **Batteriebetrieb** schaltet das Stromkreismodul auf **216 V Gleichspannung** aus der Batterie um.
- Die Betriebsgeräte in den Leuchten sind für **beides** gebaut: 220–240 V AC und **176–264 V DC**. Deshalb braucht eine CPS **keinen Wechselrichter**. Die Module heißen bei INOTEC folgerichtig **„Stromkreisumschaltungen“** (*change-over modules*).
- DC-Stromkreise müssen **2-polig abgesichert** werden (DIN VDE V 0100-560-1). Die CF-Module haben eine 2-polige Absicherung je Stromkreis.

### 7.2 Stromkreismodule (Einschübe) der CPS FUSION
| Modul | Stromkreise | Max. Last je Kreis | Sicherung (Original mit Löschmittel) | Abschaltvermögen |
|-------|-------------|--------------------|--------------------------------------|------------------|
| **CF 4x1A** | 4 | 1 A | 1,6 AT (080 085) | 1.500 A |
| **CF 2x2,5A** | 2 | 2,5 A | 4 AT (080 073) | 1.500 A |
| **CF 1x5A** | 1 | 5 A | 8 AT (080 089) | 1.500 A |
| **CP 2x2,5A / 24V** | 2 (SELV, Schutzklasse III) | 2,5 A | 5 AT (080 035) | 50 A |

- Daten CF 4x1A: U<sub>N</sub> 230 V AC 50/60 Hz bzw. 176–264 V DC, **max. Einschaltstrom 250 A für 500 µs** je Stromkreis.
- **Nummerierung:** Einschub.Stromkreis, z. B. **4.1** = Einschub 4, Stromkreis 1. Bei CF 2x2,5A gelten nur die Klemmen x.1/x.2, bei CF 1x5A nur x.1.
- Das 24-V-Modul belegt **zwei Steckplätze**. Es wird **von rechts nach links** bestückt, die Stromkreisnummern richten sich nach dem Steckplatz (15, 13, 11 …).
- Module nur im **spannungsfreien** Zustand wechseln.
- **LEDs auf den CF-Modulen:**
  - rot dauernd: Leuchtenstörung
  - rot, 1 LED blinkt 3 s: Stromkreis hat Überlast
  - rot, blitzt (0,5 s): keine Ausgangsspannung
  - rot, 4 LEDs blinken schnell: Busstörung
  - gelb: Dauerlicht eingeschaltet
- **Verbraucher ohne FUSION-Betriebsgerät** dürfen nicht an einen FUSION-Stromkreis. Sie stören die Datenkommunikation. Polung L+/N− beachten: Verpolung führt zu Kommunikationsproblemen.

### 7.3 Normregeln für Endstromkreise (DIN VDE V 0100-560-1:2022-10)
- **Max. 20 Leuchten je Endstromkreis** und **max. 60 %** des Bemessungsstroms der Überstromschutzeinrichtung.
- **Ab 2 Leuchten in einem Brandabschnitt** werden sie **abwechselnd auf mindestens 2 Stromkreise** verteilt, jeder in einem eigenen Kabel. Fällt ein Kreis aus, bleibt es nicht dunkel.
- Keine AFDDs (Brandschutzschalter) in Stromkreisen der Sicherheitsbeleuchtung. Wenn RCDs nötig sind, dann einen eigenen RCD je Stromkreis.
- Max. Spannungsfall im Endstromkreis 4 % (DIN VDE 0100-520).
- Leuchten der Sicherheitsbeleuchtung kennzeichnen, z. B. mit einem roten Schild ≥ 30 mm Durchmesser.

### 7.4 Schaltungsarten
| Schaltungsart | Netzbetrieb | Netzausfall | Typischer Einsatz |
|---------------|-------------|-------------|-------------------|
| **Dauerlicht (DL)** | an | an | Rettungszeichen, wo sich ortsunkundige Personen aufhalten |
| **Bereitschaftslicht (BL)** | aus | an | Sicherheitsleuchten über Fluren und Treppen |
| **Geschaltetes Dauerlicht** | mit dem Lichtschalter an/aus | an | Leuchte, die auch als normale Beleuchtung dient |
| **Gedimmtes Dauerlicht** | gedimmt an | an (voll) | blendfreie Rettungszeichen in dunklen Räumen |
| **Dynamisch** | nach Programmierung | Richtungsanzeige je nach Lage | Dynamische Fluchtweglenkung (D.E.R.) |

- Bei der CPS FUSION ist das **pro Leuchte** einstellbar. Die Begriffe „Joker“/„gesch. Joker“ bedeuten hier nur „Mischbetrieb im Stromkreis“. Alte Joker-Module kann man nicht anschließen.
- Jeder Leuchte kann man bis zu **2 Schalteingänge** zuweisen, dynamischen Leuchten bis zu **8**. Bei 24-V-D.E.R. hat Eingang 8 die höchste Priorität.
- **Nachlaufendes Notlicht** bis 15 min: Die Sicherheitsbeleuchtung bleibt nach Netzwiederkehr noch an, bis die Allgemeinbeleuchtung wieder voll hell ist (wichtig bei Leuchtmitteln mit Anlaufzeit).
- **Handrückschaltung:** In betriebsmäßig verdunkelten Räumen (Kino, Theater) darf das Notlicht **nicht automatisch** zurückschalten. Es geht erst aus, wenn jemand am Gerät oder per Fernüberwachung quittiert (DIN VDE V 0100-560-1, 560.9.11).

### 7.5 Isolationsüberwachung
- Im Batteriebetrieb (Funktionstest, Betriebsdauertest, Netzausfall) werden alle Stromkreise auf Isolationsfehler überwacht. Grenzwert **< 470 kΩ** → Anzeige „Isolationsfehler“.
- **ISO-Test** im Menü: prüft die Messeinrichtung (simuliert). Laut Handbuch **halbjährlich**. Er **ersetzt nicht** die Isolationsmessung nach DIN VDE 0100.

---

## 8. Leuchten und Betriebsgeräte (FUSION-Technik)

- Jede FUSION-Leuchte hat ein **Betriebsgerät mit fester ID**, also eine Adressierung **ohne Adressschalter**. Die Leuchtenadresse wird der individuellen ID zugeordnet.
- **Bidirektionale Kommunikation** über die Versorgungsleitung: Die Anlage sendet Befehle (an/aus/dimmen) und bekommt Statusmeldungen zurück.
- **Typen (Auszug):**
  - **FLD 230/8-CC-320-C**: LED-Treiber mit Einzel-LED-Überwachung, 1–8 LEDs in Reihe, 320 mA konstant, max. 8 W, Netzstrom 45 mA, Einschaltstrom 5,5 A/22 µs, mit PFC
  - **FLD 230/8-CC-650-C**: 1–4 LEDs, 650 mA
  - **…/S-Varianten**: zusätzlich ein 230-V-Schalteingang (geschaltetes Dauerlicht oder lokale Phasenwächterfunktion)
  - **FLDD 230/8-CC-125-300-C**: mehrkanalig, jeder LED-Ausgang einzeln schalt-, dimm- und blinkbar (für dynamische Zeichen)
  - **FMD 230/5-120-C/S**: Überwachungsmodul für fremde Leuchten von 5–120 W, erkennt eine Störung ab 25 % Stromabweichung
- **Einzel-LED-Überwachung:** Sie erkennt nicht nur die Unterbrechung, sondern auch den **Kurzschluss einer einzelnen LED**. Laut INOTEC fallen > 97 % der defekten LEDs durch Kurzschluss im Chip aus. Ohne diese Erkennung kann eine Leuchte mit nur einer LED dunkel sein, ohne dass die Anlage etwas meldet.
- **Dauerlichtleuchten** werden **permanent** überwacht, nicht nur beim Funktionstest.
- **Learn-Mode:** Die Anlage misst die Referenzströme jeder Leuchte im AC- und DC-Betrieb (automatisch bei der Erstprogrammierung). Nach einem Leuchtentausch lernt man neu ein. Die Leuchten müssen dabei funktionstüchtig sein.
- **Stromkreisprüfung:** prüft, ob jedes angemeldete Betriebsgerät physisch am richtigen Stromkreis hängt. Empfohlen nach jeder Installation.
- Nach jeder behobenen Leuchtenstörung muss man einen **Funktionstest** auslösen, sonst bleibt die Meldung stehen.

---

## 9. Baustein 5: Steuerung, Überwachung und Kommunikation

### 9.1 TFT-Touch-Steuerteil
- 5"-Touchdisplay in der Tür, USB-Anschluss (Stick, Tastatur), Reset-Taster, LAN-Schnittstelle.
- Verwaltet bis 128 Stromkreise / 2.560 Leuchten, Zielorttexte bis 32 Zeichen bis auf Leuchtenebene.
- **Passwort** werkseitig „0000“. Der Geräteschutz aktiviert sich nach 3 min ohne Bedienung.
- **Startbildschirm:** Anlagentyp, Softwarestand, Datum/Uhrzeit, farbiges Statusfeld, drei Felder (Leuchten, Batterie mit Spannung/Strom/Kapazität, Komponenten), vier Schaltflächen unten (Menü, Funktionstest, Favoriten, Hilfe).
- **Statusfarben:**
  - **Grün:** Betrieb
  - **Gelb:** Netzausfall HV oder UV, Funktionstest oder Betriebsdauertest aktiv, Handrückschaltung, Notlichtnachlauf
  - **Rot:** Gerät gestört, Isolationsfehler, Tiefentladeschutz, blockiert mit Störung
  - **Grau:** blockiert ohne Störung
- **Menü:** Test (FT, ISO-Test, BT-Test, Tiefentladeschutz testen), Funktionen (Blockieren/Freigeben, Handrückschaltung quittieren, Tiefentladeschutz quittieren, Ladung einschalten), Info (Störungsinfo, Geräteinfo, Prüfbuch, BCS-Prüfbuch, System), USB (Konfiguration laden/speichern, Prüfbuch speichern, Update), Einstellungen (Gerät, Netzwerk, Datum/Uhrzeit, Sprache, automatische Tests, Lüfter, Passwort, Service: Stromkreisprüfung, Learn-Mode).
- **Konfiguration:** über die Windows-Software **INOTEC Konfigurator**, übertragen per USB-Stick oder LAN. Sie wird im nichtflüchtigen Speicher abgelegt.
- **Prüfbuch:** elektronisch und nichtflüchtig, mit Datum, Uhrzeit, Eintragsnummer. Export per USB.
- **Automatische Prüfeinrichtung nach DIN EN 62034:2013.** Automatischer Funktionstest in festen Intervallen; automatischer Betriebsdauertest einmal pro Jahr möglich. Das Handbuch sagt aber: *„Die jährliche Überprüfung darf nicht automatisch ausgelöst werden!“* Man startet sie also manuell bzw. begleitet sie.

### 9.2 Meldungen und Schnittstellen
- **RIF 5** (werkseitig eingebaut): 5 potentialfreie Meldekontakte (Betrieb, Batteriebetrieb, Störung, Option 1, Option 2), Fernschalteingang FS, Stromschleife SL, Temperaturfühler T, Überwachung von Hauptverteiler und Batteriespannung. Je Steuerteil nur **ein aktives** RIF 5, betrieben am **IB1**.
- **MTB (Fernmeldetableau):** LEDs grün (Betrieb), gelb (Batteriebetrieb), rot (Störung) und ein Schlüsselschalter zum Blockieren. Anschluss am RIF 5, max. 500 m bei 0,8 mm². Damit erfüllt man die **tägliche Sichtprüfung** an einer ständig besetzten Stelle.
- **CPS FUSION-MTB:** zentrales Tableau über den RTG-Bus, 2 Stränge à max. 8 Geräte, Klartext bis auf Leuchtenebene.
- **INOWeb:** Statusanzeige im Webbrowser (im Steuerteil integriert). Funktionstest/Betriebsdauertest starten, blockieren/freigeben, E-Mail-Benachrichtigung.
- **INOView:** zentrale Überwachungssoftware für viele INOTEC-Anlagen (Client/Server, Grundrisse, zentrales Prüfbuch).
- **Gebäudeleittechnik:** Modbus/TCP standardmäßig; BACnet, OPC, LON, KNX über Gateway optional.

### 9.3 Busse im Überblick
| Bus | Wofür | Hinweis |
|-----|-------|---------|
| **IB1** | intern: Stromkreismodule, aktives RIF 5 | – |
| **IB2** | Geräte-Bus extern: BUS-Unterstationen CPUSB, LSA-Module, DPÜ/B | 3-adrig (IB, +24 V, ⊥) |
| **IB3** | nur für DPÜ/B.2 | DPÜ/B entweder an IB2 oder an IB3, nicht gemischt |
| **RTG** | externe Überwachung (INOView, CPS-MTB), Unterstationen | max. 500 m |
| **BCS-Bus** | Batteriesensoren | 2-adrig |

**Leitungslängen:** IB1/IB2/IB3 und RTG max. **500 m gesamt** (mind. 0,5 mm²). 24-V-Stromschleife max. 500 m bei 0,5 mm² bzw. 2.000 m bei 1,5 mm². Ein IB-Repeater (max. einer) verstärkt den Bus und braucht eine externe 24-V-Versorgung.

---

## 10. Erweiterungen

- **CPUS FUSION (Unterstation):** eigene Steuereinheit, kein Ladeteil. Braucht vom Hauptgerät eine **Netzleitung** und eine **Batterieleitung**. Die Batterieleitung muss in **Funktionserhalt** liegen, weil sie im Notbetrieb die Unterstation versorgt. Je nach nationaler Vorschrift kann die Netzzuleitung auch vom lokalen Unterverteiler kommen. Wichtig: Der Betriebsdauertest des Hauptgeräts ist nur aussagekräftig, wenn die Unterstationen mitlaufen.
- **CPUSB FUSION (BUS-Unterstation):** Stromkreismodule an einem anderen Ort, z. B. direkt im Brandabschnitt. Versorgung über eine **3-adrige Versorgungsleitung (L+, N−, PE) in Funktionserhalt**, Kommunikation über den **3-adrigen Bus IB2**. **Fällt der Bus aus, schalten alle Stromkreise ein** (sicherer Zustand). Varianten: /16 (16 Module), /8-1 (Adressen 1–8), /8-9 (Adressen 9–16), /1-1A und /1-2,5A (Wandgehäuse mit einem Modul, eigene Stromschleife SL und Fernschalter FS, Adressschalter).
- **LSA 3.1 / LSA 8.1 (Lichtschalterabfrage):** Sicherheitsleuchten werden zusammen mit der Allgemeinbeleuchtung geschaltet. LSA 3.1: max. 8 Stück, 3 Eingänge, nur IB2. LSA 8.1: max. 3 Stück, 8 galvanisch getrennte Eingänge, integrierte DPÜ/B (gleiche Adresse). Es gibt jeweils 24-V- und 230-V-Varianten. Mit einem **invertierten** Eingang kann man selektiv einen Stromkreis bei Phasenausfall einschalten.
- **LSA 8.1/D.E.R./24V:** Schnittstelle zur **Brandmeldeanlage** (potentialfreie Kontakte) für die dynamische Fluchtweglenkung. Es zählt nur der erste Brandfall. Max. 2 je Steuerteil.

---

## 11. CPS FUSION vs. CPS 220/64 (Vorgänger)

| Merkmal | CPS 220/64 | CPS FUSION |
|---------|-----------|------------|
| Einführung | 2007 (erste mit TFT-Display) | aktuelle Generation (Katalog 2023) |
| Stromkreismodule | CP 4x2A, CP 2x4A, CP 1x6A, CP D.E.R. 2x2,5A, CP 24V | CF 4x1A, CF 2x2,5A, CF 1x5A, CP 2x2,5A/24V |
| Mischbetrieb | JOKER: Schaltungsart am Modul in der Leuchte | FUSION: Schaltungsart je Leuchte am Steuerteil |
| Überwachung | unüberwacht, Stromkreis- oder Einzelleuchtenüberwachung je Kreis | Einzelleuchten- und Einzel-LED-Überwachung, permanent bei DL |
| Stromkreise | bis 128 | bis 128 |
| Batterie | 216 V Blei | 216 V Blei |

Die 5 Bausteine, die Batterietechnik, die Normen und die Prüfungen sind identisch. Unterschiedlich sind vor allem die Module und die Leuchtenkommunikation.

---

## 12. Inbetriebnahme, Ein- und Ausschalten

**Grundregel:** Netz und Batterie **nie unter Last** schalten. Vorher die Endstromkreise wegschalten, d. h. die Anlage blockieren.

**Einschalten (Reihenfolge!):**
1. Netz einschalten
2. Ladeteil einschalten
3. Batteriesicherungen einsetzen (vorher Polarität prüfen!)

**Ausschalten (Reihenfolge!):**
1. Anlage blockieren (NL + DL)
2. Batteriesicherungen entfernen
3. Netz abschalten

**Vor der Inbetriebnahme:**
- Bus- und Datenleitungen auf Anschluss und Polung prüfen, externe Baugruppen prüfen, Stromschleife SL+/SL− am RIF 5 prüfen.
- **Isolationsmessung** der Endstromkreise an X3: komplettes System freischalten und gegen Wiedereinschalten sichern; **L und N brücken**; nur PE gegen L/N messen; **max. 500 V DC, 1 mA**; Messgerät nach DIN VDE 0413. **Nicht** an Stromkreisen mit INOTEC-24-V-Leuchten messen, die Leuchten werden zerstört.
- Batterien vor der ersten Funktionsprüfung **mind. 24 h** laden. Lagerung ohne Ladung max. 3 Monate.

**Grundeinstellungen:**
- Bei mehreren Anlagen eine eindeutige **Anlagennummer 1–63** vergeben.
- **Nennbetriebsdauer korrekt einstellen** (sonst stimmt die Batteriezustandsberechnung nicht).
- Danach eine **Stromkreisprüfung** durchführen.

---

## 13. Prüfungen (Herstellerangaben + Normen)

Laut INOTEC-Handbuch der CPS FUSION (orientiert an DIN VDE V 0108-100-1 / EN 50172):

| Intervall | Was | Wie an der CPS FUSION |
|-----------|-----|-----------------------|
| **täglich** | Sichtprüfung der Betriebsbereitschaft | Display ansehen oder Meldung an eine ständig besetzte Stelle (MTB, INOWeb, GLT): betriebsbereit / Notlichtbetrieb / gestört |
| **wöchentlich** | Umschaltung auf die Batterie und Funktion der Leuchten | **Funktionstest (FT)**, automatisch oder manuell |
| **monatlich** | Netzausfall simulieren, jede Leuchte im Batteriebetrieb prüfen, Überwachungseinrichtungen prüfen | FT + Prüfung der DPÜ |
| **halbjährlich** | Isolationsüberwachung prüfen | **ISO-Test** |
| **jährlich** | **Betriebsdauertest** über die volle Nennbetriebsdauer; Leuchten vorhanden, sauber, funktionstüchtig; Ladeeinrichtung prüfen | **BT-Test**, **nicht automatisch** auslösen; anschließend Batterie wieder laden |
| **3-jährlich** (Handbuch) / mind. 5-jährlich (EN 50172:2024) | Beleuchtungsstärke nach EN 1838 messen | Luxmeter |
| **3-jährlich** | wiederkehrende Prüfung durch **Prüfsachverständige** (Prüfverordnung des Bundeslandes, bei Sonderbauten) | – |

- **Nach dem Betriebsdauertest** ist die Batterie bis zur Wiederaufladung nicht voll. Darum nur zu Zeiten mit geringem Risiko testen oder Ersatzmaßnahmen treffen.
- **Batterieinspektion** (DIN EN IEC 62485-2): Ladespannung, Block- und Gesamtspannung, Sauberkeit/Dichtigkeit, fester Sitz der Verbinder, Lüftung, Ventile, Temperatur. Defekte Blöcke sofort tauschen.
- **Batterieprotokoll jährlich** mit mindestens: Raumtemperatur, Ladespannung/-strom, Entladestrom, Block- und Gesamtspannungen bei Belastungsbeginn und -ende. Das ist die Grundlage für Garantieansprüche.
- **Prüfbücher mind. 4 Jahre** aufbewahren.
- Normenstand und Übergangsfristen stehen in [02-normen-und-regeln.md](02-normen-und-regeln.md).

---

## 14. Typische Meldungen und erste Schritte (Fehlersuche-Basis)

| Meldung / Symptom | Wahrscheinliche Ursache | Erster Schritt |
|-------------------|-------------------------|----------------|
| Leuchtenstörung | Leuchte/LED defekt, Leuchte getauscht ohne Learn-Mode, Verpolung | Menü → Info → Störungsinfo; Leuchte prüfen/tauschen; danach Funktionstest |
| Netzausfall UV (ohne echten Ausfall) | Stromschleife offen: DPÜ ausgelöst, Brücke fehlt, Leitung unterbrochen; bei DPÜ/B Busstörung | Schleife SL+/SL− durchmessen, DPÜ-LEDs ansehen, Menü Komponenten → DPÜ/B |
| Isolationsfehler | Erdschluss in einem Endstromkreis (z. B. Feuchtigkeit in einer Außenleuchte) | Stromkreise über Trennklemmen einzeln messen (System freischalten!) |
| Busstörung (4 LEDs blinken schnell) | IB-Leitung unterbrochen/verpolt, Adresskonflikt, Repeater ohne 24 V | Busleitung und Adressen prüfen; CPUSB schaltet dann sicher EIN |
| Überlast (1 LED blinkt 3 s) | zu viele/falsche Verbraucher am Kreis, Kurzschluss | Last und Leuchtenzahl prüfen (max. 20, max. 60 %) |
| Tiefentladeschutz (rot) | Batterie nach langem Netzausfall leer, z. B. weil Notlicht nicht blockiert war | Ursache klären, quittieren, Batterie laden, später Kapazität prüfen |
| BCS: Ladung abgeschaltet | einzelner Block mit Unter-/Überspannung oder Übertemperatur | BCS-Prüfbuch und Sensor-LEDs prüfen, Block tauschen, Ladung manuell einschalten |
| Gerät blockiert (grau/rot) | Blockierung am Steuerteil, Fernschalter oder MTB-Schlüssel | Freigeben dort, wo blockiert wurde |

### 6.6 Batterie in der Praxis (Ergänzung für Folge 5)
Quellen: Zumtobel-Gebrauchsanweisung verschlossene Bleibatterien (04/10), Banner StandBy Bull (12/21), INOTEC Handbuch 2025 (Lüftung, Fragenkatalog 24–27), MAN 708199 (Kap. 3.2, 4, 6.2), Discover Battery (Temperatur), TAB-Datenblatt OPzS, Hawker-Gebrauchsanweisung (Nachfüllen).

**Bauarten**
- Nur **ortsfeste Bleibatterien** (EN 60896-11/-21/-22), Gebrauchsdauer ≥ 10 Jahre bei 20 °C, **keine Kfz-Starterbatterien** (MAN 708199).
- **Verschlossen** (OGi-Blöcke, Elektrolyt im Vlies oder als Gel): wartungsfrei, **kein Wasser nachfüllen**, Überdruckventile **nicht öffnen** (zerstört die Batterie). Trotzdem regelmäßige Inspektion nötig (Zumtobel).
- **Geschlossen** (z. B. **OPzS**, Röhrchen-/Panzerplatten, flüssiger Elektrolyt, DIN 40736): regelmäßig **destilliertes/gereinigtes Wasser nachfüllen**, Raum muss belüftet sein. Säuredichte nach Herstellerangabe, z. B. 1,24 ± 0,01 kg/l bei 20 °C (TAB-Datenblatt OPzS). **OPzV** = Panzerplatten mit Gel, verschlossen, wartungsfrei.
- Bei geschlossenen Batterien im Schrank: innen ein Schild „säurehaltig/alkalisch + Erste Hilfe bei Elektrolytkontakt“, außen ein Schild „Explosionsgefahr, keine offenen Flammen“ (MAN 708199).

**Temperatur**
- Ideal 20 °C (Zumtobel), 20 °C ± 5 °C (Banner). Wärmer verkürzt die Lebensdauer, kälter verringert die verfügbare Kapazität.
- Faustregel (Arrhenius, Herstellerangabe Discover Battery): **je 10 °C mehr etwa halbe Lebensdauer** (Beispiel: 15 Jahre bei 20 °C → 7,5 Jahre bei 30 °C).
- Dauertemperaturen > 45 °C vermeiden, 55 °C Grenze (Banner). Temperaturunterschiede zwischen Blöcken: > 3 °C durch Aufstellung vermeiden, Abstand ≥ 0,5 cm (Zumtobel); > 5 °C Abweichung → Kundendienst (Banner).
- **Temperaturkompensation der Ladespannung: Quellen unterscheiden sich.** Zumtobel: ± 3 mV/Zelle je K Abweichung von 20 °C (z. B. 30 °C → 2,27 V/Zelle). Banner: −5 mV/Zelle je °C, aber erst außerhalb 15–25 °C nötig.

**Laden, Entladen, Lagern**
- Erhaltungsladung 2,27–2,30 V/Zelle; volle Kapazität neuer Batterien erst nach **4–5 Wochen** Erhaltungsladung (Banner).
- **Nach Entladungen, auch Teilentladungen, sofort laden, spätestens nach 24 h** (Banner).
- Richtwerte Entladeschlussspannung (Zumtobel): > 3 h **1,80 V/Zelle**, 1–3 h **1,75 V/Zelle**, 20 min–1 h 1,67 V/Zelle, < 20 min 1,60 V/Zelle. → CPS 220/64 194 V (1,80), FUSION 185 V (1,71), Gessler 189 V nach 1 h (1,75).
- Lagerung: frostfrei, trocken, sauber; ohne Erhaltungsladung alle 3 Monate Ausgleichsladung (Zumtobel). INOTEC: max. **3 Monate ohne Ladung**; bei längerer Netzunterbrechung **Batteriesicherungen ziehen**; vor der ersten Funktionsprüfung mindestens 24 h laden. Entladene Batterien können einfrieren (Banner).
- Ruhespannung vor dem Einbau (20 °C): 2-V-Zelle ≥ 2,10 V, 12-V-Block ≥ 12,60 V, sonst nachladen (Banner).

**Inspektion und Protokoll (Zumtobel 7.2, Banner 5/6)**
- **Alle 6 Monate:** Sichtprüfung (Sauberkeit, Beschädigung, lose Kontakte), Erhaltungsladespannung gesamt und je Block, Oberflächentemperatur der Blöcke, Raumtemperatur.
- **Mindestens alle 12 Monate:** zusätzlich alle Anschlüsse mit Drehmomentschlüssel nachziehen und **Blockspannungen während der Entladung** (Betriebsdauertest) aufzeichnen. Das ist die **Garantiegrundlage** (Zumtobel verlangt für Reklamationen die zwei letzten Wartungsberichte).
- Blockspannung bei 2,27 V/Zelle (Banner): 12-V-Block 13,20–13,92 V (erste 6 Monate), danach 13,32–13,80 V.
- Anzugsdrehmomente Insertschraubpole (Banner): M5 5 Nm, M6 7 Nm, M8 10 Nm (± 10 %). Immer die Angabe des jeweiligen Batterieherstellers nehmen.
- Reinigen nur mit Wasser ohne Zusatz (Kunststoffteile), sauber und trocken halten gegen Kriechströme.

**Sicherheit**
- Schutzbrille und Schutzkleidung (EN 50272-2/62485-2), keine Werkzeuge oder Gegenstände auf die Batterie legen, Pole stehen immer unter Spannung, Kurzschlüsse vermeiden, kein Feuer/Funken. Schwefelsäure ätzend: Augen/Haut sofort mit viel Wasser spülen, Arzt. Blöcke sind schwer: Transportvorrichtung. Altbatterien ins Recycling (Zumtobel).
- Batterie anschließen (MAN 708199): Lieferung prüfen, **isoliertes Werkzeug**, Drehmoment des Batterieherstellers, **Batteriesicherungen vorher entfernen**, Blöcke mit Polverbindern verschalten, **Schutzkappen auf die Pole**, bei BCS die Adapter unter die Polverbinder, Batteriesicherungen erst nach Abschluss der Installation einsetzen, auf Polung achten.

**Aufstellraum und Lüftung (INOTEC Handbuch 2025, nach DIN EN IEC 62485-2)**
- Schutzziel H₂ < 4 Vol.-%; dann gilt der Raum nicht als explosionsgefährdet (Abs. 7.2).
- Q = 0,05 · n · I<sub>gas</sub> · C<sub>N</sub> · 10⁻³ m³/h mit **I<sub>gas</sub> = 1 mA/Ah bei Erhaltungsladung, 8 bei Starkladung**; für Sicherheitsbeleuchtung ist laut Anhang A.3 I<sub>gas</sub> = 1 anzusetzen. A = 28 · Q cm² je Zu- und Abluftöffnung.
- Beispiel 216 V/70 Ah: Q = 0,378 m³/h. Eine dichtschließende Rauchschutztür hat bis 9 m³/h Leckrate (DIN 18095-1), also das 23-Fache.
- Fragenkatalog 24: verschlossene 216 V/100 Ah → Öffnungen je ca. **16 cm²**, geschlossene gleicher Kapazität → mind. **76 cm²**.
- Boden: auf Gewicht ausgelegt; bei geschlossenen Batterien elektrolytbeständig oder Auffangwanne; in Armreichweite ableitfähig < 10 MΩ (oder Gummimatte); > 120 V DC Zugang eingeschränkt (Verriegelung); abschließbare Anti-Panik-Tür nach außen.
