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
			<form id="idWTForm" name="Login" onsubmit="return checkLoginData();" action="/Zuordnen" method="POST">
				<h2>Prüfer Zuordnen</h2>
				<hr />
				<table>
					<tr>
						<th>Name</th><th>Matrikelnr.</th><th>1. Prüfer</th><th>2. Prüfer</th>
						<th>Aktionen</th>
					</tr>
						<tr>
							<td>${vars[5]} ${vars[4]}</td><td>${vars[6]}</td>
                            <td>
                                    <select name="pruefer1" id="pruefer1" value="${vars[0]}" id="type_s">
                                        <option value=" "> </option>
                                        % for key_s in data_b:
                                                ##hier müssen noch FB mitglieder übergeben werden
                                                    <option id="f${key_s}" value="${key_s}">${data_b[key_s][3] + ' ' + data_b[key_s][2]} </option>

                                        % endfor
                                    </select>
                            </td>
                            <td>
                                    <select name="pruefer2"  id="pruefer2" value="${vars[1]}" id="type_s">
                                        <option value=" "> </option>
                                        % for key_s in data_o:
                                            % if int(key_s) != 0:
                                                <option id="s${key_s}" value="${key_s}">${data_o[key_s][3] + ' ' + data_o[key_s][2]} </option>
                                            % endif
                                        % endfor
                                    </select>
                            </td>
							<td><a href="/PrüferZuordnen/${vars[0]}" class="btn">Prüfer Zuordnen -></a></td>
						</tr>
				</table>
			</form>
        </div>
    </body>
</html>