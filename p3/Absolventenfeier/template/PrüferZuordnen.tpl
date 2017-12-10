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
        <script src="/absolventenfeier.js"></script>
    </head>
    <body>
        <a href="/index" class="header-link">
            <div class="header-bg">
                <h1>Absolventenfeier</h1>
            </div>
        </a>
        <div class="content">
			<form id="idWTForm" action="/submitZuordnung" method="POST">

				<input type="hidden" value="${vars[10]}" id="id_s" name="id_s" />
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
                                    <select name="pruefer1" id="pruefer1" class="${vars[0]}">
                                        <option id="empty1" value="empty"> </option>
                                        % for key_s in data_b:
                                            <option id="f${key_s}" value="${key_s}">${data_b[key_s][3] + ' ' + data_b[key_s][2]} </option>

                                        % endfor
                                    </select>
                            </td>
                            <td>
                                    <select name="pruefer2"  id="pruefer2" class="${vars[1]}" >
                                        <option id="empty2" value="empty"> </option>
                                        % for key_s in data_o:
                                            % if int(key_s) != 0:
                                                <option id="s${key_s}" value="${key_s}">${data_o[key_s][3] + ' ' + data_o[key_s][2]} </option>
                                            % endif
                                        % endfor
                                    </select>
                            </td>
							<td><input class="btn" type="submit" value="Prüfer Zuordnen ->" /></td>
						</tr>
				</table>
			</form>
        </div>
    </body>
</html>