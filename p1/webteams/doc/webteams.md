% Gruppe I 
% Jonas Kuschel, Leon Beer
% 23.10.2017

# Aufbau der Webanwendung

##Struktur

\\ app

> \\ application.py
	
> \\ database.py
	
> \\ view.py
	
\\ content

> \\ form0.tpl
	
> \\ form1.tpl
	
> \\ form2.tpl
	
> \\ list0.tpl
	
> \\ list1.tpl
	
> \\ list2.tpl
	
> \\ Reset.css
	
> \\ webteams.css
	
> \\ webteams.js
	
\\ data

> \\ webteams.json

\\ doc

> \\ webteams.html

> \\ webteams.md

\\ server.py


## application.py

> Erzeugt die Antworten zu entsprechenden Anfragen an den Server. Ist die Schnittstelle zum Server.

### index

> Führt auf die Startseite also die Liste.

### add

> Ruft die Formularseite auf um einen neuen Eintrag zu erstellen.

### edit

> Ruft die Formularseite auf um einen bestehenden Eintrag zu editieren.

### save

> Speichert das Formular in der .JSON Datei.

### delete

> Löscht den Eintrag aus der Liste und zeigt die Liste neu an.

### default

> Falls eine unbekannte Anforderung an den Webserver geschickt wird hiermit der Fehler ausgegeben.

## database.py

> Kümmert sich um Datenbank Anfragen. Editiert also die .JSON Datei.

## view.py

> Erzeugt die Anzeige für den User. Verknüpft dafür die .tpl zu einem Vollständigen HTML Document.

## __init__.py

> Kennzeichnet ein Verzeichnis als Python-Package.

##form0.tpl

> Enthält den Kopfteil des Formulars. 

##form1.tpl

> Enthält Teile des Body Bereichs. Dieser Bereich wird für Eingaben genutzt.

##form2.tpl

> Enthält das Ende des Dokuments. Hier wird der Speichern und Abbrechen Button angezeigt.

##list0.tpl

> Enthält den Kopfteil des Dokuments. Hier wird auch der Kopteil der Tabelle beschrieben.

##list1.tpl

> Enthält die Zeilen der Tabelle des Dokuments

##list2.tpl

> Enthält das Ende des Dokuments. Außerdem ist hier der Link zur erfassen Seite.

## Reset.css

> Hier werden alle Standard CSS Änderungen zurückgesetzt.

## webteams.css

> Hier wird die Webseite verschönert. Style Anpassungen können hier gemacht werden.
	
## webteams.js

> Hier wird das Löschen Event in der Liste abgefangen. Außerdem wird das Confirm-Popup implementiert, welches bei der Betätigung des Löschvorgangs 
in der Liste geöffnet wird. Der Löschvorgang kann durch die Confirm Message abgebrochen werden.

## webteams.json

> Hier werden die Daten der Anwendung gespeichert.

## webteams.html

> Dokumentation des Projektes in HTML Form.

## webteams.md

> Dokumentation des Projektes in Markdown Form.

## server.py

> Startet den Webserver. Besitzt die main() Funktion. Initilisiert cherrypy.

# Durchgeführte Ergänzungen

## application.py

> SemsterAnzahl für beide Gruppenmitglieder hinzugefügt.

data_a = [ data_opl["name1_s"]

        , data_opl["vorname1_s"]
		
        , data_opl["matrnr1_s"]
		
        , data_opl["semestAnzahl1_s"]
		
        , data_opl["name2_s"]
		
        , data_opl["vorname2_s"]
		
        , data_opl["matrnr2_s"]
		
        , data_opl["semestAnzahl2_s"]
		
        ]

## database.py

> Die delete_px() Funktion wurde erweitert. Hier wird die das aktuelle Element auf den Default
Wert zurückgesetzt.

		self.data_o[id_spl] = self.getDefault_px()

		status_b = True
		
> Default um 2 neue Werte erweitert um die Semesteranzahl fassen zu können.

## form1.tpl

> Die Input Felder für die Semesteranzahl und den 2. Teamkollegen wurden hinzugefügt.

## list0.tpl

> Die Überschrift für die Semesteranzahl wurde hinzugefügt.

## list1.tpl

> Die Spalten für die Semesteranzahl wurden hinzugefügt. Außerdem wurde in den delete Link
die Klasse (class="clDelete") hinzugefügt.

## webteams.js

> Es wurde eine Abfrage hinzugefügt die Testet, ob der User die Gruppe wirklich
löschen möchte.

		if (!confirm("Do you want to continue deleting?")) {
            event_opl.preventDefault();
        }

# Beschreibung des HTTP-Datenverkehrs

## beim Start der Anwendung

* Methode `GET /` -> index

* Methode `GET /webteams.js`

* Methode `GET /webteams.css`

* Methode `GET /reset.css`


## beim Speichern von Formulardaten

* `POST /save`




