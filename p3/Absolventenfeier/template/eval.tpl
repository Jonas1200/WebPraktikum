## coding: utf-8
<!DOCTYPE html>
<html>
    <head>
        <title>Absolventenfeier</title>
        <meta charset="UTF-8" />
        <style>
            @import "/reset.css";
            @import "/absolventenfeier.css";
        </style>
        <script type="text/javascript" src="/absolventenfeier.js"></script>
    </head>
    <body>
        <a href="/index" class="header-link">
            <div class="header-bg">
                <h1>Absolventenfeier</h1>
            </div>
        </a>
        <div class="content">
            <h2>Datenpflege und Auswertung</h2>
            <hr />
            <table> <!-- HIER müssen Sie eine Ergänzung vornehmen -->
                <tr>
                    <th>Absolventenfeier</th><th>Begin</th><th>Ende</th><th>Beschreibung Preisverleihung</th>
                    <th>Aktionen</th><th>Navigation</th>
                </tr>
                %  for key_s in data_o:
                    %  if int(key_s) != 0:
                        <tr>
                            <td>${data_o[key_s][0]}</td><td>${data_o[key_s][1]}</td><td>${data_o[key_s][2]}</td><td>${data_o[key_s][3]}</td>
                            <td><a href="/editAbsolventenfeier/${key_s}" class="btn">Bearbeiten</a>&nbsp;<a href="/deleteAbsolventenfeier/${key_s}" class="clDelete">Löschen</a></td>
                            <td><a href="/TeilnahmeListe/${key_s}" class="btn ">Teilnehmer</a></td>
                        </tr>
                    %endif
                % endfor
            </table>
            <div>
                <a href="/addAbsolventenfeier" class="btn">Absolventenfeier hinzufügen</a>
                <a href="/AbsolventenListe" class="btn">Alle Absolventen</a>
            </div>
        </div>
    </body>
</html>