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
            <h2>Absolventen</h2>
            <hr />
            <table>
                <tr>
                    <th>Name</th><th>Matrikelnr.</th><th>evtl. Prüfer</th>
                    <th>Aktionen</th><th>Navigation</th>
                </tr>
                %  for key_s in data_o:
                    %  if int(key_s) != 0:
                        <tr>
                            <td>${data_o[key_s][3]} ${data_o[key_s][2]}</td><td>${data_o[key_s][4]}</td><td></td><td></td>
                            ##<td><a href="/editAbsolventenfeier/${key_s}" class="btn">Bearbeiten</a>&nbsp;<a href="/deleteAbsolventenfeier/${key_s}" class="clDelete">Löschen</a></td>
                            <td><a href="/PrüferZuordnen/${key_s}" class="btn">Prüfer Zuordnen -></a></td>
                        </tr>
                    %endif
                % endfor
            </table>
        </div>
    </body>
</html>