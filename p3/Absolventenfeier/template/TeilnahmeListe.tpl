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
            <h2>Teilnahmeliste - ${vars}</h2>
            <hr />
            <table>
                <tr>
                    <th>Absolvent</th><th>Begleitpersonen</th>
                    <th>Aktionen</th>
                </tr>
                %  for key_s in data_o:
                    <tr>
                        <td>${data_o[key_s][0]}</td><td>${data_o[key_s][1]}</td>
                        ##<td><a href="/editAbsolventenfeier/${key_s}" class="btn">Bearbeiten</a>&nbsp;<a href="/deleteAbsolventenfeier/${key_s}" class="clDelete">Löschen</a></td>
                    </tr>
                % endfor
            </table>
        </div>
    </body>
</html>