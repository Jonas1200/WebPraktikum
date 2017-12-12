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

##AbsolventenfeierListeAB.tpl

>Dieses Dokument zeigt alle existierenden Absolventenfeiern an. Über diese Seite
können die Daten des Absolventen angepasst werden.
Auf diese Seite kann man nur über die Registrierung oder die Anmeldung gelangen.

##AbsolventenfeierListeFB.tpl

>Dieses Dokument zeigt alle existierenden Absolventenfeiern an. Über diese Seite
können die Daten des Fachbereichsmitgliedes angepasst werden.
Auf diese Seite kann man nur über die Registrierung oder die Anmeldung gelangen.

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

## absolventenfeier.css

> Hier wird die Webseite verschönert. Style Anpassungen können hier gemacht werden.
	
## absolventenfeier.js

> Hier wird das Löschen Event in den Absolventenfeiern abgefangen. Außerdem wird das Confirm-Popup implementiert, welches bei der Betätigung des Löschvorgangs 
in der Liste geöffnet wird. Der Löschvorgang kann durch die Confirm Message abgebrochen werden.
Hier wird auch die Passwort validierung und die Email Überprüfung implementiert.

## Absolvent.json

> Hier werden die Daten der Absolventen gespeichert.

## FB.json

> Hier werden die Daten der Fachbereichsmitglieder gespeichert.

## Absolventfeier.json

> Hier werden die Daten der Absolventenfeiern gespeichert.

## AbsolventPrüfer.json

> Hier sind die Zuordnungen der Prüfer zu den Absolventen gespeichert.
In der ersten Stelle wird die Absolventen ID gespeichert. Die zweite Stelle 
ist vom 1. Prüfer und die dritte Stelle vom 2. Prüfer des Absolventen belegt.
Jede Zuordnungen besitzt eine eigene ID.

## AbsolventAnmeldung.json

> Hier werden die Daten der Anmeldungen an Absolventenfeiern von Absolventen gespeichert.

## FBAnmeldung.json

> Hier werden die Daten der Anmeldungen an Absolventenfeiern von FB gespeichert.

## bmf.html

> Dokumentation des Projektes in HTML Form.

## bmf.md

> Dokumentation des Projektes in Markdown Form.

##AbschlussarbeitenListe.tpl

> Hier werden alle Abschlussarbeiten mit den jeweiligen Absolventen angezeigt.
Die Liste ist in Bachelor und Master Arbeiten unterteilt. Außerdem können hier
die zugeordneten Prüfer angezeigt werden.

##AbsolventenListe.tpl

> Über dieses Template werden alle sich im System befindlichen Absolventen angezeigt.
Über diese Seite kann man weiter zur Prüfer Zuordnungen gelangen.

##eval.tpl

> Auf dieses Template gelangt man wenn man auf der Startseite auf "Datenpflege und Auswertung"
klickt. Hier können die Absolventfeiern verwaltet werden, Teilnahme Listen angezeigt, Prüfer
zugeordnet und eine Liste der Abschlussarbeiten angezeigt werden.

##PrüferZuordnen.tpl

> Hier können den Absolventen Prüfer zugeordnet werden. Als 1. Prüfer können nur Professoren
ausgewählt werden. Außerdem kann ein Professor nicht 1. und 2. Prüfer sein. Als 2. Prüfer
kommen auch Fachbereichsmitglieder in Frage. 

##TeilnahmeListe.tpl

> Dieses Template kann über die "eval" Seite aufgerufen werden. Hier werden alle Teilnehmer einer
Absolventenfeier aufgelistet. 

##updateAbsolventenfeier.tpl

> Über dieses Template können die Parameter einer Absolventenfeier angepasst werden.

## server.py

> Startet den Webserver. Besitzt die main() Funktion. Initilisiert cherrypy.

# Datenablage

>Die Daten werden in JSON Dateien abgelegt. Die Absolventen sind hier von den FB Mitgliedern getrennt.
Jeder Absolvent oder FB Mitglied kann sich nur an einer Absolventenfeier anmelden.


# Konfiguration

>Ich habe für die Konfiguration eigene Seiten gebaut sodass die Daten Konfiguration
über die Webseite abgehandelt werden kann. 

# Ergebnis

> Das Ergebnis der Überprüfungen war, dass keine Fehler gefunden wurden.