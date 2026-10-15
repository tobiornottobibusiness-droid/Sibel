# Praxisbeispiel Transfer: ABB Kaufel viaFlex CPS (Foto vom Nutzer, 15.10.2026)

> Quellen: Typenschild-Foto des Nutzers (Kundenname und Gerätenummern bewusst weggelassen) und ABB viaFlex Betriebsanleitung 490.01.DE.04 (07/2021), gelesen über ManualsLib (siehe `quellen.md`). Die Anlage ist von 2017. Damals galt die Ausgabe 490.01.DE.02 (02/2017), die das gleiche Kapitel „Unterstation tauschen“ enthält. Menüs können je nach Softwarestand leicht abweichen.
> Anlass: Frage, wie man eine Unterstation spannungsfrei macht, um sie zu tauschen. Gut für Folge 9 (Unterstationen), Folge 11 (Wartung) und Folge 13 (Transfer).

## Typenschild
- ABB Kaufel GmbH, Sicherheitsstromversorgung nach EN 50171, Gerätetyp **viaFlex CPS**, Baujahr KW 2017/10
- Netz 3/N/PE AC 400 V 50 Hz 139 A, Vorsicherung 160 A gG, Leistungsaufnahme 78,6 kVA
- U<sub>Nenn</sub>/I<sub>Lade</sub> 220 V / **75 A**, Verbraucherstrom 227,3 A
- Batterie **108 × 2 V OPzS 1200** (geschlossene Bleibatterie, 1.200 Ah), Batteriespannung **max. 259,2 V** (= 2,40 V/Zelle, Starkladung), Überbrückungszeit **3 h**
- Schranktyp S9 & Gestell, Umgebung +5 … 40 °C, IP20
- Service-Aufkleber: Kaufel „powered by Truvion“, Truvion GmbH, zentraler Kundendienst 0800/5352833(5), Wartungsvertrag vorhanden

## Systemaufbau (laut Anleitung und ABB)
- viaFlex ist die Nachfolgerin von Kaufel Sentara (ABB-Produktseite). Bestandteile: **CPS** (Zentrale mit Batterie, Ladeteil, Bedieneinheit viaFlex Touch), **Unterstationen viaFlex US** mit den Stromkreisen, Leuchtenbausteine **FLX**, PC-Software **viaFlex PRO**.
- Die Unterstationen arbeiten laut ABB autonom. Sie steuern ihre Leuchten auch dann weiter, wenn die Kommunikation zur Zentrale ausfällt.
- **Versorgung einer US:** über **2-polige Sicherungen in den Strangabgängen der CPS** zu den Unterstationen. Bei gemeinsamen Strangleitungen über **E30-Kleinverteiler** sitzen die Sicherungen dort. Bezeichnungen: Sicherungsliste in Teil 2 der Anlagendokumentation. Einspeiseleitung in Funktionserhalt E30.
- Im Netzbetrieb liegt an der US eine **Wechselspannung in Höhe der Netzspannung** aus der CPS an. Bei Netzausfall kommt Batteriespannung (Gleichspannung, bis max. 259,2 V laut Typenschild).
- Zusätzlich hat die US eine **Einspeisung aus der Allgemeinen Stromversorgung (AV)**, also aus der örtlichen Verteilung. Sie darf laut Anleitung erst eingeschaltet werden, **wenn die Versorgung aus der CPS anliegt**. Eine US hat also **zwei Einspeisungen**.
- Schalteingänge SW 1–4 (US-Modul) und SW 5–12 (I8-Modul) für potentialfreie Kontakte: Netzüberwachung 1–4, Schaltfunktionen 1–5, DS Ein/Aus, Quittierung BS(M), **US aktivieren/blockieren**. Netzüberwachung und US aktivieren/blockieren mit Leitungsüberwachung (Widerstände, viaFlex 2NUE bzw. viaFlex MLF).
- „Blockieren“ gibt es bei viaFlex als Funktion **US aktivieren/blockieren** (externer Kontakt) und als **CPS Dauerschaltung aktivieren/blockieren** je Unterstation (Funktionen → CPS Dauerschaltung). Beides ist eine Steuerfunktion und **keine Freischaltung**.
- Option „verkürzter Batteriebetrieb“ je US: kürzere Überbrückungszeit als die CPS, danach schaltet die US ab.

## Warnhinweise der Anleitung (Kapitel 1)
- Das Gerät arbeitet mit Netz- **und** Batteriespannung. Arbeiten an aktiven Geräten nur durch Fachkräfte.
- Vor dem Öffnen der Batteriesicherungen liegen bis zu **300 V DC** an.
- **Das Abschalten der allgemeinen Stromversorgung bedeutet keine Sicherheit für Wartungsarbeiten.** Bei längerer Netzunterbrechung die Batterie elektrisch vom Gerät trennen.
- Gerät nie ohne angeschlossenen Neutralleiter einschalten. Ersatzteile nur gleichen Typs oder vom Hersteller freigegeben.
- Batteriesicherungen erst nach dem Zuschalten des Gleichrichters einsetzen (Lichtbogen am Sicherungskontakt vermeiden). Bezeichnungen in der Anleitung: Netz F101–F103, Batterie F111 (+) / F112 (−).

## Unterstation tauschen (Kapitel 4.10, Anleitung 07/2021 S. 53–55)
1. Vorher eine gültige **Anlagenkonfiguration sichern** („In Datei speichern“, Kap. 3.2.2) und die **FLX-Konfigurationsdatei exportieren** (Kap. 3.5.3). Möglichst **nur eine US gleichzeitig** tauschen und sonst nichts an der Anlage ändern, damit die Parameter übernommen werden können.
2. In viaFlex PRO die US auswählen. Wenn die Seriennummer erscheint, noch keinen Haken setzen, sondern den **Service-PIN an der US länger als 5 s drücken**, dann „Weiter“ (S/N wird freigegeben).
3. US erneut auswählen → **„Trennen“** → „Weiter“. Meldung: US getrennt.
4. **Nach der Freischaltung** das Unterstationsmodul physisch tauschen. (Wie freigeschaltet wird, beschreibt das Kapitel nicht. Daraus abgeleitet: 2-polige Strangsicherung in der CPS bzw. im E30-Kleinverteiler **und** AV-Einspeisung, dann 5 Sicherheitsregeln.)
5. Neue US anmelden (Kap. 3.3.1) und suchen (Kap. 3.3.2), auswählen → „Verbinden“ → „Weiter“.
6. Funktionen → **Konfiguration übertragen** → „Aus Datei laden“ → „An Anlage senden“ (nur für die ausgewählte US). Alternativ neu parametrieren (Kap. 3.4).

## Offene Punkte (nicht in der Anleitung gefunden)
- In welcher **Reihenfolge** CPS-Strangsicherung und AV-Einspeisung beim Freischalten abgeschaltet werden sollen, und wie man die US vorher **lastfrei** macht. Risiko: Fällt die AV weg, kann die US das als Netzausfall werten und ihre Leuchten aus der CPS einschalten. Dann würde man die Strangsicherung unter Last ziehen. → Mit Betriebsanweisung, Kollegen oder Kaufel/Truvion-Kundendienst klären.
- Ob „Trennen“ in der Software die Ausgänge der US abschaltet oder nur die Anmeldung löst.
