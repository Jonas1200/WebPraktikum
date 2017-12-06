% Gruppe I 
% Jonas Kuschel, Leon Beer
% 14.11.2017

# Aufgabe der Webanwendung

>Die Webanwendung wird genutzt um Absolventen und Mitgliedern des Fachbereiches
die Möglichkeit zu geben sich an einer Absolventenfeier anzumelden.
Es besteht außerdem die Möglichkeit Daten zu den jeweiligen Personen zu
hinterlegen.

>Es besteht die Möglichkeit sich als Absolvent oder Fachbereichsmitglied
zu Registrieren und sich auch später noch einzuloggen um die Anmeldung
an eine Feier zu bearbeiten. Daher ist auch das Abmelden von einer Absolventenfeier möglich.

# Komponenten des Servers

## application.py

> Erzeugt die Antworten zu entsprechenden Anfragen an den Server. Ist die Schnittstelle zum Server.

## database.py

> Kümmert sich um Datenbank Anfragen. Editiert also die .JSON Datei.

## view.py

> Erzeugt die Anzeige für den User. Verknüpft dafür die .tpl zu einem Vollständigen HTML Document.

## __init__.py

> Kennzeichnet ein Verzeichnis als Python-Package.

##list*.tpl

>Dieses Dokument zeigt alle existierenden Absolventenfeiern an.
Es ermöglicht über einen link das erstellen von neuen Absolventenfeiern.
Auf diese Seite kann man nur über die Registrierung oder die Anmeldung gelangen.
Die Seite kann nicht direkt aufgerufen werden. Manche list Elemente
werden für die Absolventenfeiern der Absolventen und der FB genutzt.

##list0.tpl

> Enthält den Kopfteil des Absolventenfeier Dokuments.
Hier wird auch der Kopteil der Tabelle beschrieben.

##list1Absolvent.tpl

> Enthält die Zeilen der Tabelle des Dokuments. Also es zeigt alle 
Absolventenfeiern an. Enthält den Absolventen spezifischen Teil

##list1FB.tpl

> Enthält die Zeilen der Tabelle des Dokuments. Also es zeigt alle 
Absolventenfeiern an. Enthält den Fachbereichsmitglied spezifischen Teil

##list2.tpl

> Enthält das Ende des Dokuments. Außerdem kann hier die Absolventenfeier.tpl
aufgerufen werden.


##login*.tpl

>Hier wird das Login und die Registrierung für Absolventen und FB Mitglieder abgehandelt.
Teile der Seite werden sowohl von den Absolventen und den FB Mitgliedern genutzt.
Diese Seite kann von der startseite aufgerufen werden. Über das Login 
gelangt man zu den Absolventenfeiern.

##Absolventenfeier.tpl

>Über diese Seite können neue Absolventenfeiern hinzugefügt werden.
Sie kann nur nach der Anmeldung/Registrierung erreicht werden.

## Reset.css

> Hier werden alle Standard CSS Änderungen zurückgesetzt.

## webteams.css

> Hier wird die Webseite verschönert. Style Anpassungen können hier gemacht werden.
	
## webteams.js

> Hier wird das Löschen Event in den Absolventenfeiern abgefangen. Außerdem wird das Confirm-Popup implementiert, welches bei der Betätigung des Löschvorgangs 
in der Liste geöffnet wird. Der Löschvorgang kann durch die Confirm Message abgebrochen werden.
Hier wird auch die Passwort validierung und die Email Überprüfung implementiert.

## Absolvent.json

> Hier werden die Daten der Absolventen gespeichert.

## FB.json

> Hier werden die Daten der Fachbereichsmitglieder gespeichert.

## Absolventfeier.json

> Hier werden die Daten der Absolventenfeiern gespeichert.

## AbsolventAnmeldung.json

> Hier werden die Daten der Anmeldungen an Absolventenfeiern von Absolventen gespeichert.

## FBAnmeldung.json

> Hier werden die Daten der Anmeldungen an Absolventenfeiern von FB gespeichert.

## bmf.html

> Dokumentation des Projektes in HTML Form.

## bmf.md

> Dokumentation des Projektes in Markdown Form.

## server.py

> Startet den Webserver. Besitzt die main() Funktion. Initilisiert cherrypy.


# Datenablage

>Die Daten werden in JSON Dateien abgelegt. Die Absolventen sind hier von den FB Mitgliedern getrennt.
Jeder Absolvent oder FB Mitglied kann sich nur an einer Absolventenfeier anmelden.


# Konfiguration

>Ich habe für die Konfiguration eigene Seiten gebaut sodass die Daten Konfiguration
über die Webseite abgehandelt werden kann. 

# Ergebnis

>Ich fand es schwierig die Anforderungen teilweise umzusetzten da es nur
eine unzureichende Dokumentation über cherrypy im Internet gibt. Ich würde
gerne wissen wie sich manche Dinge umsetzen lassen ohne javascript zu nutzen.