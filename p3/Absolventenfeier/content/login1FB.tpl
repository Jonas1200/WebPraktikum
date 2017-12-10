                <form id="idWTForm" name="Login" onsubmit="return checkLoginData();" action="/submitLoginFB" method="POST">
                    <h2>FB</h2>
                    <hr />
                    <div>
                        <label for="user_s">Email</label>
                        <input type="email" class="input-field" id="user_s" onkeyup="checkEmail();" name="user_s" required />
                        <span id="userCheck"></span>
                    </div>
                    <div >
                        <label for="password_s">Passwort</label>
                        <input onkeyup="checkPassword()" type="password" class="input-field" id="password_s" name="password_s" required />
                    </div>