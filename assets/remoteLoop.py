from remoteHandler import RemoteComaJudgeHandler
from commandLineHandler import CommandLineHandler
from testHandler import TestHandler

cmd = CommandLineHandler()
filename = cmd.file
testing = TestHandler(filename)
remote = RemoteComaJudgeHandler(cmd.username, cmd.pwd_getter, "Documents/PA06")

try:
    remote.connect()
    cmd.loop(remote, testing)
finally:
    remote.closeConnection()
'''
comajudge result -p PA06 erst 4 minuten nach submission:
Dec 10 18:06 10_12_2017-18_02.info

Executing: comajudge result -p PA06

Du hast noch nichts fuer die Programmieraufgabe
                     PA06
abgegeben. Es kann also kein Ergebnis angezeigt werden.

Executing: comajudge submit -t Documents/PA06/p006_stefani_387416.py -p PA06


Die Abgabe wurde auf den Server geladen.
Warte einen Moment und verwende dann den Befehl

   $ comajudge result -p <Name_der_Programmieraufgabe>

um herauszufinden, ob sie vom CoMaJudge erfolgreich
abgenommen wurde.



Executing: comajudge result -p PA06


Abgabe wird noch bearbeitet. Probiere es in ein paar Minuten noch einmal.



Executing: comajudge result -p PA06 (leere datei)


Deine letzte Abnahme war nicht erfolgreich.

Dein Programm hatte einen Fehler beim Durchlaufen:

Syntaxfehler in der Funktion eulertour


Executing: comajudge submit -t Documents/PA06/p006_stefani_387416.py -p PA06

Keine Veraenderungen in der Abgabedatei.
Es wurde nichts an den Server gesendet.


Executing: comajudge submit -t Documents/PA06/p006_stefani_387416.py -p PA06


Die Wartezeit zwischen zwei Abgaben ist noch nicht verstrichen.



Executing: comajudge submit -t Documents/PA06/p006_stefani_387416.py -p PA06


Die Abgabe wurde auf den Server geladen.
Warte einen Moment und verwende dann den Befehl

   $ comajudge result -p <Name_der_Programmieraufgabe>

um herauszufinden, ob sie vom CoMaJudge erfolgreich
abgenommen wurde.



Executing: comajudge result -p PA06


Abgabe wird noch bearbeitet. Probiere es in ein paar Minuten noch einmal.



Executing: comajudge result -p PA06


Deine letzte Abnahme war nicht erfolgreich.

Dein Programm hatte einen Fehler beim Durchlaufen:

TypeError


Deine letzte Abnahme war nicht erfolgreich.

Dein Programm hatte einen Fehler beim Durchlaufen:



Deine letzte Abnahme war nicht erfolgreich.

Dein Programm hat zu lang gebraucht und musste vorzeitig beendet werden.




'''
