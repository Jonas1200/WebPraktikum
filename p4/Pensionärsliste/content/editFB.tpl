<!DOCTYPE html>
<html>
    <head>
        <title>Web-Teams</title>
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
		<form id="idWTForm" action="/confirmEditFB" name="Login" onsubmit="return checkLoginData();" method="POST">
                    <h2>Absolvent</h2>
                    <hr />
                    <div>
                        <label for="user_s">Email</label>
                        <input type="email" class="input-field" id="user_s"  value="$user_s" name="user_s" hidden />
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
                        <label for="degree_s">Akademischer Grad</label>
                        <input type="text" class="input-field" id="degree_s" value="$degree_s" name="degree_s" required />
                    </div>
                    <div>
                        <input class="btn" type="submit" value="Weiter" /><a href="/index" class="btn">Zurück</a>
                    </div>     
               </form>
        </div>        
    </body>
</html>						