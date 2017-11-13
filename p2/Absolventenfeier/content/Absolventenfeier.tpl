<!DOCTYPE html>
<html>
    <head>
        <title>Web-Teams</title>
        <meta charset="UTF-8" />
        <style>
            @import "/reset.css";
            @import "/webteams.css";
        </style>
        <script type="text/javascript" src="/webteams.js"></script>
    </head>
    <body>
        <a href="/index" class="header-link">
            <div class="header-bg ">
                <h1>Absolventenfeier</h1>
            </div>
        </a>
        <div class="content">
            <form id="idWTForm" action="/submitAbsolventenfeier" method="POST">
                <table>
                    <tr>
                        <div>
                            <td><label for="absolventenfeier_s">Absolventenfeier Name</label></td>
                            <td><input type="text" class="input-field" id="absolventenfeier_s" name="absolventenfeier_s" required /></td>
                        </div>
                    </tr>
                    <tr>
                        <div >
                            <td><label for="begin_t">Begin</label></td>
                            <td><input type="time" class="input-field" id="begin_t" name="begin_t" required /></td>
                        </div>
                    </tr>
                    <tr>
                        <div >
                            <td><label for="end_t">Ende</label></td>
                            <td><input type="time" class="input-field" id="end_t" name="end_t" required /></td>
                        </div>
                    </tr>
                    <tr>
                        <div>
                            <td><label for="beschreibung_s">Beschreibung Preisverleihung</label></td>
                            <td><input type="text" class="input-field" id="beschreibung_s" name="beschreibung_s" required /></td>
                        </div>
                    </tr>
                </table>
                    <div>
                        <input type="submit" value="Speichern" /><input type="reset" value="Abbrechen"/>
                    </div>            
            </form>
        </div>        
    </body>
</html>