---
titel: Folge 7 – Stromkreise: Module, Sicherungen, Joker, Lichtschalterabfrage und Isolationsmessung
datei: folge-07-stromkreise
---
# Folge 7 – Stromkreise

> Sprecher: SABINE = Expertin, TIM = Elektrofachkraft, neu in der Sicherheitsbeleuchtung.
> Fakten: wissensbasis/04-cps-220-64.md (Abschnitt 3, 4), wissensbasis/01-cps-fusion-anlage.md (Abschnitt 7), wissensbasis/02-normen-und-regeln.md (Abschnitt 6), MAN 708199 Kap. 6.3.2.10, 6.3.4.3, 7.2, 8.6.1.2. Transfer: wissensbasis/05-praxisbeispiel-gessler-sibelon.md und wissensbasis/06-praxisbeispiel-kaufel-viaflex.md.
> Alle Zahlen ausgeschrieben.

## Rückblick auf Folge sechs

SABINE: Hallo und willkommen zu Folge sieben. Wie immer starten wir mit drei Fragen zur letzten Folge. Erst nachdenken, dann kommt die Lösung.
SABINE: Frage eins. Woher bekommen die Leuchten ihren Strom, wenn das Netz in einer Unterverteilung der Allgemeinbeleuchtung ausfällt, die Anlage selbst aber noch Netz hat?
[PAUSE 7]
TIM: Die angeschlossenen Leuchten gehen in Dauerlicht, aber mit Wechselspannung aus dem Netz der Anlage. Die Batterie wird geschont. Erst wenn das Netz am Hauptverteiler ausfällt, geht alles auf die Batterie.
SABINE: Klasse. Frage zwei. Warum öffnet der Kontakt einer D-P-Ü bei Netzausfall, statt zu schließen?
[PAUSE 6]
TIM: Wegen des Fail-safe-Prinzips. Jede Unterbrechung der Schleife schaltet das Licht ein, auch ein abgerissener Draht oder eine kaputte D-P-Ü.
SABINE: Sehr gut. Frage drei. Wann laufen die vierundzwanzig-Volt-Netzteile im Schrank?
[PAUSE 6]
TIM: Immer. Sie versorgen das Gehirn der Anlage, also Steuerung, Relais und Überwachung. Und der erste Blick bei einem Verdacht geht auf die Leuchtdiode D-C O-K.
SABINE: Genau. Heute geht es um Baustein vier, die Stromkreise. Also um den Weg von der Anlage bis zur Leuchte. Wir schauen uns die Stromkreismodule an, ihre Sicherungen und Leuchtdioden, die Regel mit zwanzig Leuchten und sechzig Prozent, die Brandabschnitte, den Joker-Mischbetrieb, die Lichtschalterabfrage und zum Schluss die Isolationsmessung, Schritt für Schritt.
TIM: Die Isolationsmessung kenne ich aus der Ausbildung. Ich bin gespannt, was hier anders ist.
SABINE: Einiges. Und genau da kann man Geräte zerstören, wenn man es falsch macht.

## Vom Modul zur Leuchte

SABINE: Jeder Stromkreis beginnt in einem Einschub im Baugruppenträger. INOTEC nennt diese Einschübe Stromkreisumschaltungen. Der Name verrät schon, was sie tun.
TIM: Sie schalten um, zwischen Netz und Batterie.
SABINE: Richtig. Im Netzbetrieb geben sie zweihundertdreißig Volt Wechselspannung auf den Stromkreis. Im Batteriebetrieb schalten sie auf die zweihundertsechzehn Volt Gleichspannung der Batterie um. Die Betriebsgeräte in den Leuchten vertragen beides. Deshalb braucht eine Zentralbatterieanlage keinen Wechselrichter.
TIM: Welche Module gibt es bei der C-P-S zweihundertzwanzig Strich vierundsechzig?
SABINE: Drei für zweihundertdreißig Volt. Das C-P vier mal zwei Ampere hat vier Stromkreise mit je zwei Ampere. Das C-P zwei mal vier Ampere hat zwei Stromkreise mit je vier Ampere. Und das C-P eins mal sechs Ampere hat einen Stromkreis mit sechs Ampere. Dazu kommen ein Modul für vierundzwanzig-Volt-Leuchten und eines für dynamische Leuchten. Bei der FUSION heißen die Module C-F, mit eins, zweieinhalb und fünf Ampere.
TIM: Und das Modul für dynamische Leuchten?
SABINE: Dynamische Leuchten zeigen im Brandfall die Fluchtrichtung an, je nachdem, wo es brennt. An der C-P-S zweihundertzwanzig Strich vierundsechzig brauchen sie dafür eine eigene Busleitung, mit den Klemmen B plus und B minus. Die darf bei null Komma fünf Quadratmillimetern bis fünfhundert Meter lang sein, bei eins Komma fünf Quadratmillimetern bis zweitausend Meter. Die Leuchten am ersten Kreis bekommen die Adressen eins bis zwanzig, am zweiten Kreis einundzwanzig bis vierzig. Erst die FUSION kommt ohne diese Busleitung aus. Die vierundzwanzig-Volt-Module und die Module für dynamische Leuchten belegen übrigens jeweils zwei Steckplätze und werden von rechts nach links bestückt.
TIM: Und wie finde ich einen bestimmten Stromkreis?
SABINE: Über die Nummer, das kennst du aus Folge vier. Vier Punkt eins heißt Einschub vier, Stromkreis eins. Beim Modul mit zwei mal vier Ampere sind nur die Klemmen Punkt eins und Punkt zwei belegt. Beim Modul mit sechs Ampere nur Punkt eins. Die anderen Klemmen haben dann keine Funktion. Die Leuchten hängen an der Klemmleiste X drei, mit L, N und P-E je Stromkreis.
TIM: Und die Module in den Unterstationen?
SABINE: Das sind dieselben Module, nur an einem anderen Ort, zum Beispiel direkt im Brandabschnitt. Im Steuerteil heißen sie externe Einschübe. Eine Bus-Unterstation bekommt ihre Energie über eine dreiadrige Versorgungsleitung mit L plus, N minus und P-E in Funktionserhalt und ihre Befehle über den Bus. So kommst du mit einer Anlage auf bis zu einhundertachtundzwanzig Stromkreise.
TIM: Kann ich so ein Modul im Betrieb ziehen und tauschen?
SABINE: Nein. Die Anleitung sagt klar: Stromkreiseinschübe nur im spannungsfreien Zustand wechseln. Also Anlage freischalten nach Anleitung und Betriebsanweisung.
TIM: Und die Leuchtdioden auf den Modulen?
SABINE: Die sind dein erster Blick bei einer Störung. Rot und dauernd an heißt Leuchtenstörung. Blinkt eine einzelne rote Leuchtdiode im Abstand von drei Sekunden, hat dieser Stromkreis eine Überlast. Blitzt die Leuchtdiode nur kurz auf, im Takt von einer halben Sekunde, fehlt die Ausgangsspannung. Blinken alle vier roten schnell, ist der Bus gestört. Und gelb heißt, das Dauerlicht ist eingeschaltet.
TIM: Und wenn eine Modulsicherung ausgelöst hat?
SABINE: Dann fehlt an diesem Stromkreis die Ausgangsspannung, und genau das zeigt die kurz blitzende Leuchtdiode. Bevor du die Sicherung ersetzt, suchst du die Ursache, zum Beispiel einen Kurzschluss in einer Leuchte oder eine Überlast, weil jemand Leuchten dazugehängt hat.
TIM: Ich fasse zusammen. Ein Modul ist eine Umschaltung zwischen Netz und Batterie. Die Nummer heißt Einschub Punkt Stromkreis. Tauschen nur spannungsfrei. Und die Leuchtdioden verraten mir, ob es eine Leuchtenstörung, eine Überlast oder fehlende Spannung ist.
SABINE: Klasse.

## Sicherungen, Einschaltstrom und die Sechzig-Prozent-Regel

SABINE: Jeder Stromkreis hat seine eigene Sicherung im Modul. Beim C-P vier mal zwei Ampere sind es drei Komma eins fünf Ampere, beim zwei mal vier Ampere sechs Komma drei Ampere und beim eins mal sechs Ampere zehn Ampere. Alle mit einem Abschaltvermögen von eintausendfünfhundert Ampere.
TIM: Kann ich da im Notfall irgendeine Feinsicherung mit dem gleichen Wert reinstecken?
SABINE: Nein, und das ist wichtig. Die Anleitung verlangt Originalsicherungen mit Löschmittel. Denk an Folge zwei: Im Batteriebetrieb fließt Gleichstrom, und der Lichtbogen in einer Sicherung geht nicht von allein aus. Das Löschmittel und das hohe Abschaltvermögen sorgen dafür, dass die Sicherung den Strom wirklich trennt. Eine beliebige Feinsicherung ist dafür nicht unbedingt ausgelegt.
TIM: Verstanden. Und warum ist das Abschaltvermögen so hoch?
SABINE: Weil hinter der Sicherung eine Batterie steht, die bei einem Kurzschluss einen riesigen Strom liefern kann. Und noch eine Zahl zum Einschalten: Der Einschaltstrom eines Stromkreises darf höchstens zweihundertfünfzig Ampere für fünfhundert Mikrosekunden betragen. Elektronische Betriebsgeräte haben beim Einschalten eine kurze Stromspitze, weil sich ihre Kondensatoren aufladen. Bei vielen Leuchten an einem Kreis addiert sich das.
TIM: Und jetzt die Regel mit den zwanzig Leuchten.
SABINE: Genau. Die Errichtungsnorm sagt: höchstens zwanzig Leuchten an einem Endstromkreis und höchstens sechzig Prozent des Nennstroms der Sicherung. Und jetzt rechne mal. Sechzig Prozent von drei Komma eins fünf Ampere sind?
TIM: Das sind etwa eins Komma neun Ampere. Aha, das passt fast genau zu den zwei Ampere pro Stromkreis beim C-P vier mal zwei Ampere.
SABINE: Richtig erkannt. Und sechzig Prozent von zehn Ampere sind sechs Ampere, genau der Wert des Moduls mit einem Stromkreis. Die Module sind also so gebaut, dass die Sechzig-Prozent-Regel aufgeht.
TIM: Warum überhaupt nur sechzig Prozent? Die Sicherung hält doch mehr aus.
SABINE: Damit Reserven da sind, für den Einschaltstrom, für Alterung, für eine Leuchte, die später dazukommt, und damit die Sicherung bei einem Fehler zuverlässig auslöst, aber im Normalbetrieb nicht. Dazu gehören noch drei Regeln. Der Spannungsfall im Endstromkreis darf höchstens vier Prozent betragen. In Stromkreisen der Sicherheitsbeleuchtung gibt es keine Brandschutzschalter. Und wenn ein Fehlerstromschutzschalter nötig ist, dann ein eigener für jeden Stromkreis, damit ein Fehler nicht mehrere Kreise abschaltet.
TIM: Warum ist der Spannungsfall hier so wichtig?
SABINE: Wegen des Batteriebetriebs. Am Ende einer langen Entladung sinkt die Batteriespannung bis auf etwa einhundertvierundneunzig Volt, dann greift der Tiefentladeschutz. Ein J-S-V-Modul von INOTEC arbeitet ab einhundertneunundsiebzig Volt Gleichspannung. Rechne vier Prozent Spannungsfall von einhundertvierundneunzig Volt ab, dann bleiben an der letzten Leuchte noch rund einhundertsechsundachtzig Volt. Das reicht. Bei einer zu langen oder zu dünnen Leitung kann die letzte Leuchte aber kurz vor Ende der Nennbetriebsdauer ausgehen, obwohl die Batterie noch nicht leer ist.

## Brandabschnitte: nie alles an einem Kreis

TIM: In Folge drei hast du gesagt, dass man die Leuchten in einem Brandabschnitt auf mehrere Stromkreise verteilt. Wie genau?
SABINE: Sobald in einem Brandabschnitt zwei oder mehr Leuchten hängen, werden sie abwechselnd auf mindestens zwei Stromkreise verteilt. Und jeder Stromkreis läuft in einem eigenen Kabel.
TIM: Warum abwechselnd?
SABINE: Stell dir einen langen Flur mit sechs Leuchten vor. Hängen die ersten drei an Kreis eins und die letzten drei an Kreis zwei, und Kreis eins fällt aus, ist die eine Hälfte des Flurs stockdunkel. Hängen sie abwechselnd, also eins, zwei, eins, zwei, bleibt bei einem Ausfall jede zweite Leuchte an. Es wird dunkler, aber man findet den Weg.
TIM: Wie die Lichterkette am Weihnachtsbaum. Wenn eine ausfällt, soll nicht der ganze Baum dunkel sein.
SABINE: Schönes Bild. Und das eigene Kabel braucht es, weil ein beschädigtes Kabel sonst beide Kreise auf einmal treffen würde. Aus Folge drei kennst du noch die zweite Regel: Ein Endstromkreis versorgt Leuchten nur in einem Brandabschnitt. Läuft eine Leitung durch mehrere Brandabschnitte, braucht sie Funktionserhalt.
TIM: Ich fasse zusammen. In jedem Brandabschnitt mindestens zwei Stromkreise, die Leuchten abwechselnd verteilt, jeder Kreis im eigenen Kabel. So bleibt bei einem Ausfall jede zweite Leuchte an. Und ein Kreis versorgt nur Leuchten in einem einzigen Brandabschnitt.
SABINE: Genau so.
TIM: Und wie sehe ich in der Praxis, ob das eingehalten ist?
SABINE: Im Plan und in der Leuchtenliste. Dort steht bei jeder Leuchte der Stromkreis und der Zielort. Haben in einem Brandabschnitt alle Leuchten dieselbe Stromkreisnummer, ist das ein Mangel, den du dem Betreiber meldest.

## Überwachung und Joker in der Praxis

SABINE: Jetzt zur Überwachung. Bei der C-P-S zweihundertzwanzig Strich vierundsechzig kannst du für jeden Stromkreis eine von drei Überwachungsarten wählen. Unüberwacht, Stromkreisüberwachung oder Einzelleuchtenüberwachung.
TIM: Was ist der Unterschied?
SABINE: Bei der Stromkreisüberwachung misst die Anlage den Strom des ganzen Kreises und vergleicht ihn mit einem Referenzwert. Den lernt sie im sogenannten Learn-Mode. Fällt eine Leuchte aus, sinkt der Strom, und die Anlage meldet einen Fehler. Sie weiß aber nicht, welche Leuchte es ist. Bei der Einzelleuchtenüberwachung hat jede Leuchte ein Modul mit einer eigenen Adresse. Dann zeigt die Anlage genau, welche Leuchte gestört ist.
TIM: Und dafür sind die Adressschalter an den Joker-Modulen.
SABINE: Genau. Jetzt kommen wir zum Joker. Das ist die patentierte Technik von INOTEC, mit der Bereitschaftslicht und Dauerlicht gemischt in einem Stromkreis laufen können. Ohne zusätzliche Datenleitung. An jeder Leuchte sitzt ein Joker-Betriebsgerät oder ein J-S-V-Modul vor einem fremden Betriebsgerät. Mit einem Mikroschalter stellst du die Schaltungsart ein, also Dauerlicht oder Bereitschaftslicht. Mit den Adressschaltern stellst du die Adresse von eins bis zwanzig ein.
TIM: Dann kann im selben Flur das Rettungszeichen immer leuchten und die Sicherheitsleuchte daneben nur im Notfall, obwohl beide am selben Kreis hängen.
SABINE: Genau das ist der Witz. Und es gibt noch einen optionalen Sense-Eingang am Leuchtenmodul. Damit kann man eine Leuchte vor Ort schalten, zum Beispiel mit dem normalen Raumlichtschalter.
TIM: Und wenn das Netz ausfällt? Bleibt die Bereitschaftsleuchte dann aus, weil der Mikroschalter auf Bereitschaft steht?
SABINE: Nein, gute Frage. Die eingestellte Schaltungsart gilt nur im Netzbetrieb. Fällt das Netz in einer überwachten Unterverteilung aus, schaltet die Anlage alle Leuchten an allen Stromkreisen ein, egal was eingestellt ist. Fällt das Netz am Hauptverteiler aus, geht ohnehin alles auf die Batterie. Im Notfall leuchtet also alles.
TIM: Und bei der FUSION?
SABINE: Dort hat jedes Betriebsgerät eine feste Kennung. Mikroschalter und Adressschalter entfallen. Die Schaltungsart wird für jede Leuchte am Steuerteil eingestellt. Ein Punkt gilt aber bei beiden: Nach jeder behobenen Leuchtenstörung startest du einen Funktionstest, sonst bleibt die Meldung stehen. Und nach einem Leuchtentausch lernt man die Referenzwerte neu ein.
TIM: Wie merkt die Anlage eigentlich, dass eine Leuchte kaputt ist?
SABINE: Über den Strom. Beim J-S-V-Modul gilt eine Leuchte als in Betrieb, wenn mehr als zwanzig Milliampere fließen, und als gestört, wenn es weniger als zehn Milliampere sind. Die FUSION geht noch weiter. Ihre Betriebsgeräte erkennen sogar, wenn eine einzelne L-E-D einen Kurzschluss hat. Laut INOTEC fallen über siebenundneunzig Prozent der defekten L-E-Ds genau so aus. Ohne diese Erkennung kann eine Leuchte mit nur einer L-E-D dunkel sein, ohne dass die Anlage etwas merkt. Dauerlichtleuchten werden bei der FUSION übrigens ständig überwacht, nicht nur beim Funktionstest.
TIM: Und wenn ich eine Joker-Leuchte tausche?
SABINE: Dann stellst du Mikroschalter und Adresse genauso ein wie bei der alten Leuchte, sonst passt die Überwachung nicht mehr. Bei der FUSION gibt es dafür eine Stromkreisprüfung. Sie prüft, ob jedes angemeldete Betriebsgerät wirklich an dem Stromkreis hängt, an dem es angemeldet ist. Den Leuchtentausch schauen wir uns in Folge acht genau an.

## Die Lichtschalterabfrage

TIM: Was macht eine Lichtschalterabfrage genau?
SABINE: Mit ihr schaltest du Sicherheitsleuchten zusammen mit der Allgemeinbeleuchtung. Stell dir einen Besprechungsraum vor. Die Sicherheitsleuchten dort sollen nicht dauernd brennen, aber wenn jemand das Licht einschaltet, sollen sie mit angehen und als normale Beleuchtung mitarbeiten. Dafür greift die Lichtschalterabfrage das Signal des Lichtschalters ab und meldet es über den Bus an die Anlage.
TIM: Welche Module gibt es?
SABINE: Zwei. Die L-S-A drei Punkt eins hat drei Eingänge, davon passen bis zu acht Stück an ein Steuerteil, und sie darf nur am Gerätebus I-B zwei hängen. Die L-S-A acht Punkt eins hat acht galvanisch getrennte Eingänge, davon passen bis zu drei Stück an ein Steuerteil, und sie hat eine Dreiphasenüberwachung mit Bus gleich eingebaut. Beide gibt es mit Eingängen für vierundzwanzig Volt oder für zweihundertdreißig Volt.
TIM: Wozu sind die Eingänge der großen galvanisch getrennt?
SABINE: Damit die Schaltsignale aus verschiedenen Stromkreisen oder von verschiedenen Phasen kommen dürfen, ohne dass du diese Kreise über das Modul miteinander verbindest. Jeder Eingang ist für sich abgeschlossen.
TIM: Gibt es etwas, worauf ich beim Anschluss achten muss?
SABINE: Ja. Die L-S-A drei Punkt eins mit zweihundertdreißig Volt hat für ihre drei Eingänge nur einen gemeinsamen Neutralleiter. Das steht ausdrücklich in der Anleitung. Und jedes Modul bekommt am Adressschalter eine eindeutige Adresse, die im Steuerteil als aktiv eingestellt wird.
TIM: Und was passiert, wenn jemand den Schalter betätigt?
SABINE: Leuchten in Bereitschaftsschaltung oder gedimmte Leuchten werden eingeschaltet. Leuchten in Dauerschaltung bleiben sowieso an. Diese Schaltungsart heißt geschaltetes Dauerlicht: Im Netzbetrieb geht die Leuchte mit dem Lichtschalter an und aus, bei Netzausfall ist sie immer an. Einem Stromkreis kann man bis zu drei Schalteingänge zuweisen. Und ein Trick: Mit einem invertierten Eingang kann man einen Stromkreis gezielt einschalten, wenn eine bestimmte Phase ausfällt.
TIM: Ich fasse zusammen. Mit der Lichtschalterabfrage geht das Sicherheitslicht zusammen mit dem normalen Licht an. Die kleine hat drei Eingänge und nur einen gemeinsamen N, die große acht getrennte Eingänge und eine Phasenüberwachung dabei.
SABINE: Sehr gut.

## Die Isolationsmessung Schritt für Schritt

SABINE: Jetzt der wichtigste Teil. Fangen wir mit dem an, was die Anlage selbst tut. Im Batteriebetrieb, also bei Funktionstest, Betriebsdauertest oder Netzausfall, überwacht sie alle Stromkreise auf Isolationsfehler. Fällt der Isolationswiderstand unter vierhundertsiebzig Kilo-Ohm, meldet sie einen Isolationsfehler.
TIM: Warum nur im Batteriebetrieb?
SABINE: Weil die Batterie nicht geerdet ist. Das ist das I-T-Prinzip aus Folge zwei. Ein einzelner Erdschluss löst noch nichts aus, aber er muss gemeldet werden, bevor ein zweiter dazukommt. Die Anlage unterscheidet übrigens zwischen Isolationsfehler plus und minus, je nachdem, ob der Pluspol oder der Minuspol der Batterie Kontakt zum Schutzleiter hat.
TIM: Und der I-S-O-Test im Menü?
SABINE: Der prüft nur, ob die Messeinrichtung der Anlage funktioniert, indem er eine Messung simuliert. Laut Handbuch macht man ihn halbjährlich. Aber er ersetzt ausdrücklich nicht die Isolationsmessung nach V-D-E null einhundert vor der Inbetriebnahme. Die machst du mit deinem Messgerät.
TIM: Dann los. Schritt für Schritt.
SABINE: Schritt eins: das komplette System freischalten, also Netz und Batterie, nach Anleitung und Betriebsanweisung, und gegen unbefugtes Wiedereinschalten sichern. Erst wenn alle Messungen fertig sind, wird wieder eingeschaltet.
SABINE: Schritt zwei, und das ist der Unterschied zu deiner Ausbildung: Du brückst L und N des Endstromkreises. Gemessen wird nur zwischen dem Schutzleiter und L sowie zwischen dem Schutzleiter und N. Nie zwischen L und N.
TIM: Warum die Brücke?
SABINE: Damit die Messspannung nicht zwischen L und N über die Elektronik der Betriebsgeräte geht. Mit der Brücke liegen L und N auf demselben Potential. Die Messspannung belastet dann nur die Isolierung gegen Erde, und genau die willst du ja prüfen.
SABINE: Schritt drei: Messspannung höchstens fünfhundert Volt Gleichspannung, Messstrom ein Milliampere, und nur mit einem Messgerät nach der Norm V-D-E null vierhundertdreizehn. Den Mindestwert für Stromkreise bis fünfhundert Volt kennst du aus der Ausbildung: ein Mega-Ohm.
SABINE: Schritt vier: Brücke wieder entfernen und zum nächsten Stromkreis. Erst eins Punkt eins, dann eins Punkt zwei, eins Punkt drei und so weiter, und auch die Stromkreise der Unterstationen.
TIM: Und die vierundzwanzig-Volt-Kreise?
SABINE: Da kommt die wichtigste Warnung. An Stromkreisen mit vierundzwanzig-Volt-Leuchten von INOTEC wird keine Isolationsmessung gemacht. Die Anleitung sagt wörtlich, dass die Leuchten dabei zerstört werden. Ihre Elektronik ist für Kleinspannung gebaut und hält fünfhundert Volt Messspannung nicht aus. Das gilt auch für die vierundzwanzig-Volt-Kreise in Bus-Unterstationen.
TIM: Und was kommt ins Protokoll?
SABINE: Für jeden Stromkreis die Nummer, die Messspannung und der gemessene Wert, dazu Datum, Messgerät und wer gemessen hat. Und ein Vermerk, welche Kreise bewusst nicht gemessen wurden, zum Beispiel die vierundzwanzig-Volt-Kreise. Dann weiß der Nächste, dass das kein Versehen war.
TIM: Ich fasse zusammen. Freischalten und sichern. L und N brücken. Nur Schutzleiter gegen L und N messen, mit höchstens fünfhundert Volt. Brücke raus, nächster Kreis. Und vierundzwanzig-Volt-Kreise nie.
SABINE: Klasse. Und wenn die Anlage im Betrieb einen Isolationsfehler meldet, suchst du genauso. Anlage freischalten, die Stromkreise über die Trennklemmen einzeln messen, bis du den Kreis mit dem niedrigen Wert gefunden hast. Typisch ist Feuchtigkeit in einer Außenleuchte oder in einer Abzweigdose. Und denk daran: Ein Isolationsfehler kann auch in Teilen sitzen, die mit der Batterie verbunden sind, also nicht nur in Leuchten, sondern zum Beispiel auch in einer Lichtschalterabfrage oder einer D-P-Ü mit Bus.

## Transfer-Ecke: Gessler und Kaufel

SABINE: Wie sieht das bei deinen anderen Anlagen aus? Im Gessler hast du die Endstromkreise schon gesehen: zwanzig Stromkreise, F eins bis F zwanzig, jeweils mit einer roten und einer blauen Sicherungsklemme. Auf dem Schild mit den Gerätedaten steht beim Teil für die Stromkreise die Angabe zwanzig S. Das steht vermutlich für die zwanzig Stromkreise.
TIM: Also zweipolig abgesichert, Plus und Minus. Genau wie die Errichtungsnorm es für Gleichstrom verlangt.
SABINE: Richtig. Bei Kaufel sitzen die Stromkreise in den Unterstationen. Jede Unterstation hat zwei Stromkreise, auf dem Modul stehen Circuit eins und Circuit zwei. An deiner US zehn hingen am siebten Stromkreis dreizehn Leuchten und am achten Stromkreis acht Leuchten.
TIM: Beide unter zwanzig. Und die Klemmen im Unterverteiler hießen C eins plus, C eins minus, C zwei plus und C zwei minus.
SABINE: Genau, auch dort zweipolig. Die Leuchten haben bei Kaufel adressierbare Bausteine, die heißen F-L-X. Deshalb musste der Assistent nach dem Tausch die Leuchten suchen. Und die Funktion F-L-X-Ströme zurücksetzen erinnert an das Neu-Einlernen der Referenzströme bei INOTEC.
TIM: Und meine Frage für den nächsten Einsatz?
SABINE: Such dir einen Flur und schau in der Leuchtenliste nach: Hängen die Leuchten dort abwechselnd an mindestens zwei Stromkreisen? Und wie viele Leuchten hängen am vollsten Stromkreis der Anlage?

## Wiederholung mit Denkpausen

SABINE: Zeit für die Wiederholung. Frage, Denkpause, dann die Lösung.
SABINE: Frage eins. Warum braucht eine Zentralbatterieanlage keinen Wechselrichter?
[PAUSE 6]
TIM: Weil die Betriebsgeräte in den Leuchten sowohl Wechselspannung als auch Gleichspannung vertragen. Das Modul schaltet nur zwischen Netz und Batterie um.
SABINE: Frage zwei. Was bedeutet eine einzelne rote Leuchtdiode, die im Abstand von drei Sekunden blinkt?
[PAUSE 6]
TIM: Dieser Stromkreis hat eine Überlast.
SABINE: Frage drei. Warum nur Originalsicherungen mit Löschmittel?
[PAUSE 7]
TIM: Weil im Batteriebetrieb Gleichstrom fließt und der Lichtbogen nicht von allein ausgeht. Die Sicherung muss bei zweihundertsechzehn Volt Gleichspannung sicher trennen, mit hohem Abschaltvermögen.
SABINE: Frage vier. Nenne die Regel für Endstromkreise und die Regel für Brandabschnitte.
[PAUSE 8]
TIM: Höchstens zwanzig Leuchten und höchstens sechzig Prozent des Sicherungsnennstroms. Ab zwei Leuchten in einem Brandabschnitt abwechselnd auf mindestens zwei Stromkreise, jeder in einem eigenen Kabel.
SABINE: Frage fünf. Gilt die eingestellte Schaltungsart auch bei Netzausfall?
[PAUSE 6]
TIM: Nein, nur im Netzbetrieb. Bei Netzausfall gehen alle Leuchten an.
SABINE: Frage sechs. Was tut die Lichtschalterabfrage?
[PAUSE 6]
TIM: Sie schaltet Sicherheitsleuchten zusammen mit der Allgemeinbeleuchtung ein, über das Signal des Lichtschalters.
SABINE: Und Frage sieben. Nenne die Schritte der Isolationsmessung und die wichtigste Ausnahme.
[PAUSE 8]
TIM: System freischalten und sichern. L und N brücken. Nur Schutzleiter gegen L und gegen N messen, mit höchstens fünfhundert Volt Gleichspannung. Brücke entfernen, nächster Kreis. Und an vierundzwanzig-Volt-Kreisen nie messen, sonst sind die Leuchten kaputt.
SABINE: Sehr gut. Damit kennst du den Weg von der Anlage bis zur Leuchte.

## Praxisauftrag und Ausblick

SABINE: Dein Praxisauftrag hat drei Teile. Erstens: Schau dir beim nächsten Einsatz die Stromkreismodule an. Welche Typen sind verbaut, und leuchtet irgendwo eine rote oder gelbe Leuchtdiode?
TIM: Und als Zweites?
SABINE: Als Zweites: Nimm die Leuchtenliste und prüf in einem Brandabschnitt, zum Beispiel an einem Flur, ob die Leuchten abwechselnd auf zwei Stromkreisen liegen. Und drittens: Such im Prüfbuch das Protokoll der letzten Isolationsmessung. Stehen dort die Werte für jeden Stromkreis, und sind die vierundzwanzig-Volt-Kreise ausgenommen?
TIM: Also die Module, die Leuchtenliste und das Messprotokoll. Mach ich.
SABINE: In Folge acht geht es um die Leuchten selbst. Rettungszeichen und Sicherheitsleuchten, Erkennungsweite und Montagehöhe, Joker-Betriebsgeräte mit Mikro- und Adressschaltern, Leuchtentausch und Einlernen, und die typischen Fehlerbilder von LED-Leuchten.
TIM: Danke, Sabine. Bis morgen!
SABINE: Bis bald, und gute Fahrt!
