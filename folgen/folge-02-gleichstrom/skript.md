---
titel: Folge 2 – Gleichstrom für Wechselstrom-Profis: Batterie, Spannungen und die Risiken bei 216 Volt
datei: folge-02-gleichstrom
---
# Folge 2 – Gleichstrom für Wechselstrom-Profis

> Sprecher: SABINE = Expertin, TIM = Elektrofachkraft (Ausbildung Energie- und Gebäudetechnik), neu in der Sicherheitsbeleuchtung.
> Referenzanlage: INOTEC CPS 220/64. Fakten: wissensbasis/04-cps-220-64.md, wissensbasis/01-cps-fusion-anlage.md, Batterie-Merkblätter (siehe quellen.md).
> Alle Zahlen ausgeschrieben.

## Rückblick auf Folge eins

SABINE: Hallo und willkommen zu Folge zwei. Bevor wir loslegen, machen wir das, was Wissen wirklich festigt: kurz abrufen, was du letztes Mal gelernt hast. Drei Fragen, jeweils mit ein paar Sekunden Denkpause.
SABINE: Frage eins. Welche fünf Bausteine hat jede Zentralbatterieanlage?
[PAUSE 8]
TIM: Netzeinspeisung mit Netzüberwachung, Ladeteil, Batterie, Umschaltung mit Endstromkreisen, und Steuerung mit Überwachung und Meldung.
SABINE: Sehr gut. Frage zwei. Eine einzelne Unterverteilung der Allgemeinbeleuchtung fällt aus. Woher bekommen die Sicherheitsleuchten in diesem Bereich ihren Strom?
[PAUSE 6]
TIM: Aus dem Netz, über die Zentralbatterieanlage. Die Anlage hat ja selbst noch Netz. Die Batterie springt erst ein, wenn auch an der Einspeisung der Anlage das Netz weg ist.
SABINE: Richtig. Und Frage drei. Warum braucht die Anlage keinen Wechselrichter?
[PAUSE 6]
TIM: Weil die Betriebsgeräte in den Leuchten sowohl Wechselspannung als auch Gleichspannung vertragen.
SABINE: Klasse. Dann zum heutigen Thema. Tim, du hast mir erzählt, dass du gelernter Elektroniker für Energie- und Gebäudetechnik bist.
TIM: Genau. Wechselstrom ist mein tägliches Brot: Drehstrom, Schutzmaßnahmen, Fehlerschutz, Messungen nach Norm, das sitzt. Aber Gleichstrom mit über zweihundert Volt, das kam in der Ausbildung nur am Rande vor. Und bei uns im Betrieb stehen fast überall Anlagen vom Typ C-P-S zweihundertzwanzig Strich vierundsechzig von Inotec.
SABINE: Dann ist diese Folge genau für dich. Wir überspringen alles, was du aus der Wechselstromwelt kennst, und konzentrieren uns auf das, was bei Gleichstrom anders ist. Erst schauen wir uns die Batterie elektrisch an. Dann rechnen wir mit Ampere-Stunden und Wattstunden. Und dann kommt der wichtigste Teil: die Risiken. Was du dir als Wechselstrom-Profi bei Gleichstrom abgewöhnen musst. Und ganz nebenbei lösen wir das Rätsel aus Folge eins: warum das Display nicht zweihundertsechzehn Volt anzeigt.

## Warum die Notbeleuchtung Gleichstrom mag

TIM: Fangen wir mit einer Frage an, die mich seit letzter Woche beschäftigt. Wie kann eine Leuchte, die für zweihundertdreißig Volt Wechselspannung gebaut ist, plötzlich mit Gleichspannung laufen?
SABINE: Schau dir an, was in einem modernen L-E-D-Betriebsgerät passiert. Ganz vorne am Eingang sitzt ein Gleichrichter, meistens eine Brückenschaltung aus vier Dioden, und dahinter ein Kondensator, der die Spannung glättet. Das Betriebsgerät macht also aus der Wechselspannung als allererstes Gleichspannung. Erst danach regelt die Elektronik den konstanten Strom für die L-E-Ds.
TIM: Ach so. Wenn ich am Eingang gleich Gleichspannung anlege, leiten im Gleichrichter einfach dauerhaft zwei Dioden, und der Rest der Schaltung merkt keinen Unterschied.
SABINE: Genau. Deshalb stehen auf den Inotec-Leuchtenmodulen zwei Spannungsbereiche: zweihundertzwanzig bis zweihundertvierzig Volt Wechselspannung, und ungefähr hundertachtzig bis zweihundertvierundsechzig Volt Gleichspannung. Diesen Gleichspannungsbereich solltest du dir merken. Er erklärt, warum die Batterie während der Entladung ruhig etwas absinken darf.
SABINE: Und bevor wir tiefer einsteigen, gebe ich dir eine Liste mit fünf Unterschieden zwischen Wechselstrom und Gleichstrom, die uns heute begleiten. Erstens: Gleichstrom hat keinen Nulldurchgang. Zweitens: Es gibt keinen Cosinus Phi, also keine Blindleistung. Drittens: Die Polarität zählt, Plus und Minus sind nicht vertauschbar. Viertens: Eine Batterie lässt sich nicht abschalten. Und fünftens: Das Gleichstromsystem der Anlage ist im Batteriebetrieb nicht geerdet. Zu jedem Punkt kommen wir gleich.

## Die Batterie elektrisch: von der Zelle zur Anlage

SABINE: Die kleinste Einheit ist die Bleizelle. Ihre Nennspannung ist zwei Volt. In einem Block stecken sechs Zellen in Reihe, das ergibt die zwölf Volt. Und achtzehn Blöcke in Reihe ergeben einhundertacht Zellen und zweihundertsechzehn Volt.
TIM: Das sind also einhundertacht Zellen. Die Zahl sollte man sich merken, oder?
SABINE: Unbedingt, denn Batteriefachleute denken immer pro Zelle. Jede Spannung, die du an der Anlage abliest, teilst du durch einhundertacht, und schon weißt du, in welchem Zustand die Batterie ist. Und jetzt kommt der wichtigste Satz zur Batterie: Die zweihundertsechzehn Volt sind nur eine Bezeichnung. Die sogenannte Nennspannung misst du fast nie.
TIM: Dann bin ich gespannt. Was zeigt das Display denn im Normalbetrieb?
SABINE: Im Normalbetrieb hängt die Batterie am Ladeteil und wird in der Erhaltungsladung gehalten. Das Ladeteil hält dabei eine feste Spannung, die je nach Batteriehersteller bei ungefähr zwei Komma zwei sieben bis zwei Komma drei Volt pro Zelle liegt, bezogen auf zwanzig Grad. Mal einhundertacht ergibt das rund zweihundertfünfundvierzig bis zweihundertachtundvierzig Volt.
TIM: Das ist also das Rätsel aus der letzten Folge. Die zweihundertvierzig und mehr auf dem Display sind die Ladespannung.
SABINE: Exakt. Und es gibt noch mehr Spannungen, die du kennen solltest. Nach einer Entladung lädt das Ladeteil die Batterie zuerst mit begrenztem Strom und dann mit etwas erhöhter Spannung wieder auf. Das nennt man Starkladung. Dabei können es bis zu zwei Komma drei fünf, im Ausnahmefall zwei Komma vier Volt pro Zelle werden. Das sind dann über zweihundertfünfzig Volt an der Anlage. Wenn der Ladestrom abgesunken ist, schaltet das Ladeteil wieder auf Erhaltungsladung.
TIM: Erst Strom begrenzen, dann Spannung halten. Das klingt nach der I-U-Kennlinie, also erst Strom, dann Spannung.
SABINE: Genau die. Und dann die andere Richtung. Wenn das Netz ausfällt, sinkt die Spannung. Zuerst fällt sie schnell von der Ladespannung herunter, dann sinkt sie langsam, je länger entladen wird. Am Ende der Nennbetriebsdauer darf sie bis etwa eins Komma acht Volt pro Zelle fallen. Mal einhundertacht sind das ungefähr hundertvierundneunzig Volt. Und genau bei hundertvierundneunzig Volt liegt laut Handbuch der Tiefentladeschutz unserer zweihundertzwanzig Strich vierundsechzig.
TIM: Und was passiert beim Tiefentladeschutz genau?
SABINE: Die Anlage trennt die Verbraucher von der Batterie, bevor die Batterie zu tief entladen wird. Eine tiefentladene Bleibatterie wird dauerhaft geschädigt, die Platten sulfatieren, und im schlimmsten Fall ist der ganze Satz hinüber. Nach einer Auslösung bleibt die Anlage in diesem Zustand, bis jemand den Tiefentladeschutz am Steuerteil quittiert. Kleine Randnotiz: Bei der neueren Fusion steht im Handbuch ein etwas niedrigerer Wert, hundertfünfundachtzig Volt. Darum immer ins Handbuch der jeweiligen Anlage schauen.
TIM: Also: Erhaltungsladung rund zweihundertfünfundvierzig Volt, Starkladung über zweihundertfünfzig, Nennspannung zweihundertsechzehn, Tiefentladeschutz hundertvierundneunzig.
SABINE: Klasse zusammengefasst. Und noch ein Wert für die Praxis: Pro Block sind das bei Erhaltungsladung ungefähr dreizehn Komma sechs bis dreizehn Komma acht Volt. Wenn ein Batterieüberwachungssystem wie das B-C-S verbaut ist, schlägt es Alarm, wenn ein Block unter zehn Komma drei Volt fällt oder über fünfzehn Volt steigt.
TIM: Und die Temperatur, spielt die eine Rolle?
SABINE: Eine riesige. Die ideale Temperatur für die Batterie ist zwanzig Grad. Wird es wärmer, muss die Ladespannung sinken, ungefähr drei Millivolt pro Zelle und Grad. Deshalb gibt es an der Anlage einen Anschluss für einen Temperaturfühler im Batterieraum, damit das Ladeteil die Spannung anpassen kann. Und Wärme lässt Batterien schneller altern. Die Norm für Zentralbatterieanlagen rechnet bei zwanzig Grad mit fünfundzwanzig Prozent Alterungsreserve. Bei dreißig Grad wären es für verschlossene Batterien über achtzig Prozent. Ein heißer Batterieraum kostet also richtig Batterielebensdauer.

## Ampere-Stunden, Wattstunden und warum es im Notfall weniger sind

TIM: Kommen wir zur Kapazität. Ampere-Stunden kenne ich vom Akkuschrauber. Ampere mal Stunden, oder?
SABINE: Genau. Eine Batterie mit zehn Ampere-Stunden kann theoretisch zehn Stunden lang ein Ampere liefern. Aber jetzt kommt eine Eigenschaft, die Wechselstromleute oft überrascht: Die Kapazität einer Batterie hängt davon ab, wie schnell du sie entlädst.
TIM: Wie meinst du das?
SABINE: Ich gebe dir ein Beispiel aus der Inotec-Batterietabelle. Der kleinste Batterietyp dort hat zwölf Ampere-Stunden, gemessen bei einer zehnstündigen Entladung. Wenn du ihn in acht Stunden entlädst, kann er ein Komma drei Ampere liefern. Das sind gut zehn Ampere-Stunden. Wenn du ihn aber in einer Stunde leer machen willst, schafft er nur sechs Komma drei Ampere. Das sind gerade mal gut sechs Ampere-Stunden.
TIM: Also nur noch die Hälfte. Je schneller ich entlade, desto weniger kommt insgesamt raus.
SABINE: Richtig. Stell dir einen Läufer vor. Im gemütlichen Dauerlauf schafft er zwanzig Kilometer. Im Sprint ist er nach ein paar hundert Metern platt, obwohl er nicht weniger trainiert ist. Bei der Batterie ist es ähnlich, die Chemie kommt bei hohen Strömen nicht hinterher. Deshalb wählt man die Batterie immer passend zur Nennbetriebsdauer aus einer Tabelle, und nicht einfach über die aufgedruckten Ampere-Stunden.
TIM: Und die Wattstunden?
SABINE: Die beschreiben die Energie. Spannung mal Ampere-Stunden. Zweihundertsechzehn Volt mal zwölf Ampere-Stunden sind ungefähr zwei Komma sechs Kilowattstunden. Das ist mehr als eine Spielerei, denn das Baurecht arbeitet mit diesen Grenzen. Nach der Muster-Verordnung für elektrische Betriebsräume sind Notlichtsysteme mit verschlossenen Batterien bis zwei Kilowattstunden ausgenommen. Bei einer Zweihundertsechzehn-Volt-Batterie entspricht das nur gut neun Ampere-Stunden. Eine typische Zentralbatterie liegt deutlich darüber.
SABINE: Jetzt zur Leistung. Bei Gleichstrom ist es angenehm einfach: Leistung gleich Spannung mal Strom. Kein Cosinus Phi, keine Blindleistung. Im Netzbetrieb haben die L-E-D-Betriebsgeräte einen Leistungsfaktor von ungefähr null Komma acht fünf bis null Komma neun acht. Deshalb steht in den Datenblättern oft eine Angabe in Voltampere. Im Batteriebetrieb zählen nur Watt.
TIM: Und wie viel Strom zieht die Anlage dann aus der Batterie?
SABINE: Hier kommt der nächste Gleichstrom-Effekt. Die Betriebsgeräte regeln auf eine konstante Leistung. Wenn die Batteriespannung im Lauf der Entladung sinkt, ziehen sie mehr Strom. Stell dir tausend Watt Last vor. Bei zweihundertsechzehn Volt sind das ungefähr vier Komma sechs Ampere. Bei hundertvierundneunzig Volt kurz vor Schluss sind es schon gut fünf Komma eins Ampere.
TIM: Die Batterie wird also gegen Ende doppelt gefordert: Die Spannung sinkt, und der Strom steigt.
SABINE: Genau deshalb ist die Batterieauslegung kein Bauchgefühl. Lass uns einmal grob überschlagen, damit du ein Gefühl bekommst. Hundert Leuchten mit je fünf Watt sind fünfhundert Watt. Geteilt durch zweihundertsechzehn Volt sind das ungefähr zwei Komma drei Ampere. Dazu fünfundzwanzig Prozent Alterungsreserve, dann landest du bei knapp drei Ampere. Bei drei Stunden Nennbetriebsdauer schaut man in die Tabelle: Der kleinste Batterietyp schafft bei drei Stunden genau drei Ampere. Das wäre also knapp.
TIM: Und in der Praxis rechnet das der Konfigurator oder der Planer.
SABINE: Ja. Aber du solltest es plausibel nachvollziehen können, zum Beispiel wenn eine Batterie beim Betriebsdauertest nicht durchhält. Zum Laden noch eine Zahl: Eine leere Batterie muss nach zwölf Stunden wieder genug Energie für achtzig Prozent der Nennbetriebsdauer haben. Deshalb macht man den jährlichen Betriebsdauertest nur zu einer Zeit, in der wenig passieren kann. Danach ist die Batterie stundenlang nicht voll.

## Die Risiken, Teil eins: Lichtbogen und Batterie

SABINE: Jetzt kommt der wichtigste Teil. Ich nenne es die sechs Gleichstrom-Regeln, also sechs Dinge, die bei Gleichstrom anders sind als bei dem, was du gewohnt bist.
SABINE: Regel eins: Der Lichtbogen geht nicht von alleine aus. Bei fünfzig Hertz Wechselstrom geht die Spannung hundertmal pro Sekunde durch null. Ein Lichtbogen beim Trennen reißt deshalb meist von selbst ab. Gleichstrom hat keinen Nulldurchgang. Wenn du einen Gleichstromkreis unter Last öffnest, kann der Lichtbogen stehen bleiben. Er brennt weiter, schmilzt Kontakte und kann Verbrennungen verursachen.
TIM: Das heißt praktisch: Klemmen, Stecker oder Sicherungen nie unter Last ziehen.
SABINE: Genau. Das ist auch der Grund für zwei Vorschriften im Inotec-Handbuch. Erstens: Netz und Batterie niemals unter Last ein- oder ausschalten, die Anlage vorher blockieren. Zweitens: In den Stromkreiseinschüben nur Originalsicherungen mit Löschmittel verwenden. Die Sicherungen sind mit Sand gefüllt, damit der Lichtbogen gelöscht wird, und haben ein Abschaltvermögen von eintausendfünfhundert Ampere. Eine normale Feinsicherung aus der Kiste kann bei einem Gleichstrom-Kurzschluss den Bogen nicht sicher löschen. Und das gilt allgemein: Schalter und Sicherungen müssen für Gleichstrom bemessen sein. Ein Bemessungswert für Wechselstrom sagt über Gleichstrom nichts aus.
SABINE: Regel zwei: Eine Batterie kann man nicht ausschalten. Wenn du die Batteriesicherungen ziehst, trennst du die Batterie vom Gerät. Die Batterie selbst bleibt aber geladen. Zwischen den Enden des Strangs liegen weiterhin rund zweihundertfünfundvierzig Volt. Und jeder einzelne Block mit zwölf Volt kann bei einem Kurzschluss schnell mehrere hundert Ampere liefern.
TIM: Zwölf Volt klingen ja harmlos.
SABINE: Für den Körper ja, für dein Werkzeug nicht. Ein Ringschlüssel, der über zwei Pole fällt, wird zur Schweißelektrode. Es gibt einen Lichtbogen, flüssiges Metall spritzt, und im schlimmsten Fall platzt der Block. Darum gilt am Batterieschrank: nur isoliertes Werkzeug, so steht es auch im Handbuch. Ringe, Uhren und Ketten ab. Polkappen drauf lassen, solange du nicht direkt an dem Pol arbeitest. Schutzbrille tragen. Und nur mit Freigabe arbeiten. Dazu kommt: Bleibatterien geben beim Laden Wasserstoff ab, vor allem bei der Starkladung. Funken und offene Flammen haben am Batterieschrank nichts zu suchen, und die Lüftung muss funktionieren.
TIM: Und weil die Spannung über hundertzwanzig Volt liegt, muss der Zugang zur Batterie ja auch beschränkt sein.
SABINE: Richtig, deshalb sind Batterieschränke und Batterieräume abgeschlossen und nur für befugte Personen zugänglich.

## Die Risiken, Teil zwei: Der N-Leiter und das Freischalten

SABINE: Regel drei, und das ist die, die Wechselstromprofis am häufigsten unterschätzen: Im Notbetrieb ist der N-Leiter kein Neutralleiter.
TIM: Das musst du erklären. In meinem Kopf ist der N immer ungefähr auf Erdpotenzial.
SABINE: Im Netzbetrieb stimmt das auch, da bekommen die Endstromkreise ganz normal Außenleiter und Neutralleiter. Aber im Batteriebetrieb schaltet die Anlage um. Dann liegt an der L-Klemme der Pluspol und an der N-Klemme der Minuspol der Batterie. Inotec bezeichnet die Klemmen bei den Unterstationen deshalb auch als L plus und N minus. Und das Gleichstromsystem ist nicht geerdet. Es ist isoliert aufgebaut und wird nur auf Isolationsfehler überwacht, so wie du es vom I-T-System kennst.
TIM: Dann sind im Batteriebetrieb also beide Leiter aktive Leiter.
SABINE: Genau. Zwischen N und Schutzleiter kann eine deutliche Spannung stehen. Daraus folgt für dich: Spannungsfreiheit immer allpolig feststellen, also zwischen L und N, zwischen L und P-E und zwischen N und P-E. Mit einem zweipoligen Spannungsprüfer, der Gleichspannung anzeigt. Und niemals den N anfassen, weil du ihn für ungefährlich hältst.
SABINE: Regel vier: Der Stromkreis wird von woanders eingeschaltet. Was machst du im Wechselstromalltag, wenn du an einer Leuchte arbeiten willst?
TIM: Ich schalte den Stromkreis in der Unterverteilung ab.
SABINE: Und genau das funktioniert bei der Sicherheitsbeleuchtung nicht. Erstens kommt der Stromkreis gar nicht aus der Unterverteilung, sondern aus der Zentralbatterieanlage. Zweitens: Wenn du die Unterverteilung der Allgemeinbeleuchtung abschaltest, meldet die Dreiphasenüberwachung einen Ausfall, und die Anlage schaltet die Sicherheitsleuchten genau dort ein. Du erzeugst also selbst Spannung an deinem Arbeitsplatz. Und drittens kann jederzeit ein automatischer Funktionstest starten und die Kreise auf Batterie schalten.
TIM: Dann muss ich an der Anlage selbst freischalten.
SABINE: Richtig. Und noch ein Punkt: Das Blockieren am Steuerteil ist eine Betriebsfunktion, keine sichere Trennung. Für die fünf Sicherheitsregeln brauchst du eine echte Trennung des Stromkreises an der Anlage. Wie das bei euch genau gemacht wird, steht in eurer Betriebsanweisung. Als Faustregel gilt: Erst lastfrei machen, damit beim Trennen kein Gleichstrom-Lichtbogen entsteht. Dann allpolig trennen, gegen Wiedereinschalten sichern, Spannungsfreiheit allpolig feststellen. Und denk daran, dass ein abgeschalteter Stromkreis an der Anlage als Störung auffallen kann. Die Arbeit gehört ins Prüfbuch, und der Betreiber muss Bescheid wissen, denn in dieser Zeit fehlt im Gebäude ein Stück Sicherheitsbeleuchtung.
SABINE: Regel fünf: Gleichstrom ist nicht harmlos. Es stimmt, dass Gleichstrom bei gleicher Stromstärke für das Herz weniger kritisch ist als Wechselstrom mit fünfzig Hertz, und das Loslassen fällt leichter. Deshalb liegt die vereinbarte Grenze für die dauernd zulässige Berührungsspannung bei Gleichstrom bei hundertzwanzig Volt und bei Wechselstrom bei fünfzig Volt. Aber unsere Anlage arbeitet mit zweihundertfünfundvierzig Volt. Das ist doppelt so viel wie diese Grenze. Dazu kommen die Lichtbögen und die Kurzschlussströme der Batterie. Respekt ist also absolut angebracht.
SABINE: Und Regel sechs: Die Polarität zählt. Bei der Erstinbetriebnahme muss vor dem Einsetzen der Batteriesicherungen die richtige Polarität der Batterie sichergestellt sein, das betont das Handbuch ausdrücklich. Eine verpolte Batterie kann Bauteile zerstören. Und auch in den Stromkreisen gilt: Plus bleibt Plus und Minus bleibt Minus. Bei den neueren Fusion-Modulen weist Inotec ausdrücklich darauf hin, dass eine Verpolung zu Kommunikationsproblemen mit den Leuchten führen kann.
TIM: Lass mich die sechs Regeln wiederholen. Eins: Der Lichtbogen geht nicht von alleine aus, also nie unter Last trennen. Zwei: Die Batterie kann man nicht ausschalten, also isoliertes Werkzeug und kein Schmuck. Drei: Im Notbetrieb ist der N ein aktiver Leiter, also allpolig prüfen. Vier: Der Stromkreis wird von woanders eingeschaltet, also an der Anlage freischalten. Fünf: Gleichstrom ist nicht harmlos. Sechs: Die Polarität zählt.
SABINE: Klasse. Wenn du nur eine Sache aus dieser Folge mitnimmst, dann diese sechs Regeln.

## Isolationsüberwachung: das I-T-Prinzip

TIM: Du hast gesagt, das Gleichstromsystem ist nicht geerdet und wird auf Isolationsfehler überwacht. Wie funktioniert das bei der Anlage?
SABINE: Stell dir vor, in einer Außenleuchte sammelt sich Feuchtigkeit, und der Pluspol bekommt eine Verbindung zum Schutzleiter. In einem geerdeten System wäre das ein Erdschluss, und die Sicherung würde auslösen. Im isolierten System passiert erst einmal gar nichts. Es fließt kein Fehlerstrom, die Leuchten leuchten weiter. Das ist ja gerade der Vorteil: Ein einzelner Fehler legt die Sicherheitsbeleuchtung nicht lahm.
TIM: Aber dann darf man ihn auch nicht einfach ignorieren.
SABINE: Genau. Kommt ein zweiter Fehler am anderen Pol dazu, hast du einen Kurzschluss über die Erde, oder an einem Gehäuse liegt eine gefährliche Spannung. Deshalb misst die Anlage im Batteriebetrieb, also bei Funktionstest, Betriebsdauertest und Netzausfall, den Isolationswiderstand aller Stromkreise. Fällt er unter vierhundertsiebzig Kiloohm, zeigt das Display einen Isolationsfehler. Und den behandelst du als dringende Störung.
TIM: Und weil der Fehler an jedem der beiden Pole auftreten kann, werden Gleichstromkreise auch zweipolig abgesichert.
SABINE: Richtig. Zwei Begriffe solltest du dabei nicht verwechseln. Am Steuerteil gibt es den I-S-O-Test. Den macht man halbjährlich. Er prüft nur, ob die Messeinrichtung der Isolationsüberwachung funktioniert. Er ersetzt keine Isolationsmessung. Die echte Isolationsmessung machst du vor der Inbetriebnahme an den Endstromkreisen nach Norm, so wie du es gelernt hast. Dabei gibt es drei Besonderheiten. Erstens: Das ganze System wird freigeschaltet. Zweitens: Du brückst L und N des Stromkreises und misst nur gegen den Schutzleiter, mit höchstens fünfhundert Volt Gleichspannung. So schützt du die Elektronik in den Leuchten. Und drittens: Niemals an Stromkreisen mit Inotec-Vierundzwanzig-Volt-Leuchten messen, die gehen dabei kaputt.

## Messen an Gleichstrom

TIM: Und beim Messen? Mein Multimeter kann ja Gleichspannung.
SABINE: Das Multimeter ist kein Problem. Stell den Gleichspannungsbereich ein. Ein Minuszeichen in der Anzeige ist bei Gleichstrom übrigens eine nützliche Information: Es zeigt dir, dass deine Messspitzen andersherum an Plus und Minus liegen. So kannst du Pole identifizieren. Beim Strom wird es aber spannender. Was für eine Stromzange hast du im Koffer?
TIM: Eine ganz normale Zange für Wechselstrom.
SABINE: Die zeigt an einem Gleichstromkreis null an, egal wie viel Strom fließt. Eine klassische Zange arbeitet wie ein Stromwandler, also mit Induktion, und dafür braucht sie einen Wechselstrom. Für Gleichstrom brauchst du eine Zange mit Hall-Sensor, oft steht darauf A-C und D-C, also Wechsel- und Gleichstrom. Und vor jeder Messung machst du einen Nullabgleich, weil diese Zangen etwas driften.
TIM: Gut zu wissen. Sonst hätte ich bei einem Funktionstest gemessen und mich gewundert, warum kein Strom fließt.
SABINE: Und noch zur Batterie: Wenn du die Blockspannungen misst, also bei der Batterieinspektion, vergleichst du die Blöcke untereinander. Bei Erhaltungsladung sollten alle ungefähr gleich sein, im Bereich von dreizehn Komma sechs bis dreizehn Komma acht Volt. Ein Block, der deutlich aus der Reihe tanzt, ist verdächtig. Er kann bei einem langen Netzausfall die ganze Batterie in die Knie zwingen, weil alle Blöcke in Reihe hängen. Genau dafür gibt es das B-C-S, das jeden Block einzeln überwacht.

## Die Schaltreihenfolge: jetzt verstehst du sie

SABINE: Zum Schluss schließt sich der Kreis. In Folge eins habe ich dir die Ein- und Ausschaltreihenfolge der Anlage nur angedeutet. Jetzt verstehst du sie. Einschalten: erst Netz, dann Ladeteil, dann die Batteriesicherungen einsetzen. Und bei der Erstinbetriebnahme vorher die Polarität der Batterie prüfen.
TIM: Und Ausschalten: erst die Anlage blockieren, also Not- und Dauerlicht, dann die Batteriesicherungen raus, dann das Netz aus.
SABINE: Und warum zuerst blockieren?
TIM: Weil dann keine Last mehr dranhängt. Dann fließt beim Ziehen der Batteriesicherungen kein Strom, und es entsteht kein Gleichstrom-Lichtbogen. Und die Leuchten gehen nicht auf Batterie, wenn ich das Netz abschalte.
SABINE: Genau so. Du siehst: Die Reihenfolge ist keine Schikane, sondern angewandte Gleichstromphysik.

## Wiederholung mit Denkpausen

SABINE: Zeit für die Wiederholung. Wie immer: Frage, Denkpause, dann die Lösung.
SABINE: Frage eins. Aus wie vielen Zellen besteht die Batterie, und warum zeigt das Display im Normalbetrieb rund zweihundertfünfundvierzig Volt statt zweihundertsechzehn?
[PAUSE 8]
TIM: Die Batterie hat einhundertacht Zellen. Im Normalbetrieb läuft die Erhaltungsladung mit ungefähr zwei Komma zwei sieben bis zwei Komma drei Volt pro Zelle. Zweihundertsechzehn ist nur die Nennspannung.
SABINE: Frage zwei. Bei welcher Spannung greift der Tiefentladeschutz der zweihundertzwanzig Strich vierundsechzig, und wie viel ist das pro Zelle?
[PAUSE 7]
TIM: Bei hundertvierundneunzig Volt, das sind etwa eins Komma acht Volt pro Zelle.
SABINE: Frage drei. Warum liefert eine Batterie mit zwölf Ampere-Stunden bei einer einstündigen Entladung nur gut sechs Ampere-Stunden?
[PAUSE 7]
TIM: Weil die nutzbare Kapazität von der Entladegeschwindigkeit abhängt. Bei hohen Strömen kommt die Chemie nicht hinterher.
SABINE: Frage vier. Warum steigt der Batteriestrom gegen Ende der Entladung?
[PAUSE 6]
TIM: Weil die Betriebsgeräte konstante Leistung ziehen. Sinkt die Spannung, steigt der Strom.
SABINE: Frage fünf. Warum ist ein Lichtbogen bei Gleichstrom gefährlicher als bei Wechselstrom?
[PAUSE 6]
TIM: Weil Gleichstrom keinen Nulldurchgang hat. Der Lichtbogen reißt nicht von alleine ab.
SABINE: Frage sechs. Im Batteriebetrieb misst du zwischen N und Schutzleiter eine Spannung. Ist das ein Fehler?
[PAUSE 7]
TIM: Nicht unbedingt. Im Batteriebetrieb ist der N der Minuspol eines nicht geerdeten Systems, also ein aktiver Leiter. Deshalb immer allpolig prüfen.
SABINE: Und die letzte Frage. Du willst an einer Sicherheitsleuchte arbeiten und schaltest dafür die Unterverteilung der Allgemeinbeleuchtung ab. Was passiert, und wie machst du es richtig?
[PAUSE 10]
TIM: Die Dreiphasenüberwachung meldet einen Netzausfall, und die Anlage schaltet die Sicherheitsleuchten erst recht ein. Richtig ist: an der Zentralbatterieanlage lastfrei machen, den Stromkreis allpolig trennen nach Betriebsanweisung, gegen Wiedereinschalten sichern, allpolig Spannungsfreiheit feststellen. Und den Betreiber informieren.
SABINE: Klasse. Wenn das sitzt, bist du sicherer unterwegs als mancher, der seit Jahren an diesen Anlagen arbeitet.

## Praxisauftrag und Ausblick

SABINE: Dein Praxisauftrag für diese Woche hat vier Teile. Erstens: Lies an deiner Anlage die Batteriespannung ab und teile sie durch einhundertacht. Liegst du bei ungefähr zwei Komma zwei sieben bis zwei Komma drei Volt pro Zelle? Und schau, ob ein Temperaturfühler oder ein B-C-S verbaut ist.
TIM: Und als Zweites?
SABINE: Als Zweites: Schau im Prüfbuch nach dem letzten Betriebsdauertest. Hat die Batterie die volle Nennbetriebsdauer geschafft? Drittens: Prüf dein Werkzeug. Zeigt dein Spannungsprüfer Gleichspannung an? Habt ihr im Betrieb eine Gleichstromzange mit Hall-Sensor? Und gibt es isoliertes Werkzeug für Arbeiten an der Batterie? Und viertens: Frag einen erfahrenen Kollegen, wie ihr bei euch einen Stromkreis der Sicherheitsbeleuchtung freischaltet, und vergleiche das mit den sechs Regeln von heute.
TIM: Batteriespannung durch einhundertacht, Prüfbuch, Werkzeug, und das Freischalten im Betrieb nachfragen. Mach ich.
SABINE: In Folge drei geht es um Recht und Normen, kompakt und praxisnah: Wer muss was prüfen, welche Normen gelten gerade, was hat sich mit den neuen Ausgaben geändert, und was heißt das für deine Arbeit an der Anlage.
TIM: Danke, Sabine. Bis zum nächsten Mal!
SABINE: Bis bald, und gute Fahrt!
