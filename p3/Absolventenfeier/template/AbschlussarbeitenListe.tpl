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
    </head>
    <body>
        <a href="/index" class="header-link">
            <div class="header-bg">
                <h1>Absolventenfeier</h1>
            </div>
        </a>
        <div class="content">
            <h2>Bachelor</h2>
            <hr />
            <table>
                <tr>
                    <th>Name 1.Prüfer</th><th>Name Absolvent</th><th>Matrikelnr.</th><th>Prüfer 2.</th>
                    ##<th>Aktionen</th><th>Navigation</th>
                </tr>
                %  for key_s in data_o:
					<tr>
						<td>${data_o[key_s][0]}</td><td>${data_o[key_s][1]}</td><td>${data_o[key_s][2]}</td><td>${data_o[key_s][3]}</td>
						##<td><a href="/editAbsolventenfeier/${key_s}" class="btn">Bearbeiten</a>&nbsp;<a href="/deleteAbsolventenfeier/${key_s}" class="clDelete">Löschen</a></td>
						##<td><a href="/PrüferZuordnen/${key_s}" class="btn">Prüfer Zuordnen -></a></td>
					</tr>
                % endfor
            </table>
			<h2>Master</h2>
            <hr />
            <table>
                <tr>
                    <th>Name 1.Prüfer</th><th>Name Absolvent</th><th>Matrikelnr.</th><th>Prüfer 2.</th>
                    ##<th>Aktionen</th><th>Navigation</th>
                </tr>
                %  for key_s in data_b:
					<tr>
						<td>${data_b[key_s][0]}</td><td>${data_b[key_s][1]}</td><td>${data_b[key_s][2]}</td><td>${data_b[key_s][3]}</td>
						##<td><a href="/editAbsolventenfeier/${key_s}" class="btn">Bearbeiten</a>&nbsp;<a href="/deleteAbsolventenfeier/${key_s}" class="clDelete">Löschen</a></td>
						##<td><a href="/PrüferZuordnen/${key_s}" class="btn">Prüfer Zuordnen -></a></td>
					</tr>
                % endfor
            </table>
        </div>
    </body>
</html>