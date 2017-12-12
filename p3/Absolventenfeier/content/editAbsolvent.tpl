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
		<form id="idWTForm" action="/confirmEditAbsolvent" name="Login" onsubmit="return checkLoginData();" method="POST">

            <input type="hidden" value="$id_s" id="id_s" name="id_s" />

            <h2>Absolvent</h2>
            <hr />
            <div>
                <label for="user_s">Email</label>
                <input type="email" class="input-field" id="user_s"  value="$user_s" name="user_s" />
            </div>
            <div >
                <label for="name_s">Name</label>
                <input type="text" class="input-field" id="name_s" value="$name_s" name="name_s" required />
            </div>

            <div >
                <label for="firstname_s">Vorname</label>
                <input type="text" class="input-field" id="firstname_s" value="$firstname_s" name="firstname_s" required />
            </div>

            <div >
                <label for="matNr_s">Matrikel Nr.</label>
                <input type="text" maxlength="7" pattern=".{0}|[0-9]{6,7}" class="input-field"  value="$matNr_s" id="matNr_s" name="matNr_s" required />
            </div>

            <div >
                <label for="company_s">Anzahl Begleitpersonen</label>
                <input type="number" min="0" max="4" class="input-field" id="company_s" value="$company_s" name="company_s" required />
            </div>
            <div >
                <label for="theme_s">Thema Abschlussarbeit</label>
                <input type="text" class="input-field" id="theme_s" value="$theme_s" name="theme_s" required />
            </div>
            <div >
                <label for="type_s">Art der Abschlussarbeit</label>
                    <select name="type_s" value="$type_s" id="type_s">
                        <option value="bachelor">Bachelor</option>
                        <option value="master">Master</option>
                    </select>
            </div>
            <div>
                <input class="btn" type="submit" value="Weiter" /><a href="/index" class="btn">Zurück</a>
            </div>
        </form>
        </div>        
    </body>
</html>						