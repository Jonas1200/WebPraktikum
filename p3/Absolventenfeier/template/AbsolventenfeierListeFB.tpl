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
            <table>
                <tr>
                    <th>Absolventenfeier</th><th>Begin</th><th>Ende</th><th>Beschreibung Preisverleihung</th>
                    <th>Aktion</th>
                </tr>
                %  for key_s in data_o:
                    %if int(key_s) != 0:
                        <tr>
                            <td>${data_o[key_s][0]}</td><td>${data_o[key_s][1]}</td><td>${data_o[key_s][2]}</td><td>${data_o[key_s][3]}</td>
                            <td><a href="/applyFB/?user=${vars}&absolventenfeier=${key_s}" class="btn btn-green">anmelden</a>&nbsp;<a href="/deleteSignInFB/${vars}" class="clDelete">abmelden</a></td>
                        </tr>
                    %endif
                % endfor
            </table>
            <a href="/editFB/${vars}" class="btn">bearbeiten</a>
        </div>
    </body>
</html>