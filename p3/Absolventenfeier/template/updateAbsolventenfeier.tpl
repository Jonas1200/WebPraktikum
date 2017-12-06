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
            <div class="header-bg ">
                <h1>Absolventenfeier</h1>
            </div>
        </a>

        <div class="content">
            <h2>Absolventenfeier bearbeiten</h2>
            <hr />
            <form id="idWTForm" action="/updateAbsolventenfeier" method="POST">

                <input type="hidden" value="${data_o[0]}" id="id_s" name="id_s" />
                <table>
                    <tr>
                        <div>
                            <td><label for="absolventenfeier_s">Absolventenfeier Name</label></td>
                            <td><input type="text" class="input-field" value="${data_o[1]}" id="absolventenfeier_s" name="absolventenfeier_s" required /></td>
                        </div>
                    </tr>
                    <tr>
                        <div >
                            <td><label for="begin_t">Begin</label></td>
                            <td><input type="time" class="input-field" value="${data_o[2]}" id="begin_t" name="begin_t" required /></td>
                        </div>
                    </tr>
                    <tr>
                        <div >
                            <td><label for="end_t">Ende</label></td>
                            <td><input type="time" class="input-field" value="${data_o[3]}" id="end_t" name="end_t" required /></td>
                        </div>
                    </tr>
                    <tr>
                        <div>
                            <td><label for="beschreibung_s">Beschreibung Preisverleihung</label></td>
                            <td><input type="text" class="input-field" value="${data_o[4]}" id="beschreibung_s" name="beschreibung_s" required /></td>
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