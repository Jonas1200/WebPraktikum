                <form id="idWTForm" name="Login" onsubmit="return checkLoginData();" action="/submitLoginFB" method="POST">
                    <h2>FB</h2>
                    <hr />
                    <table>
                        <tr>
                            <div>
                                <td><label for="user_s">Email</label></td>
                                <td><input type="email" class="input-field" id="user_s" onkeyup="checkEmail();" name="user_s" required /></td>
                                <td><span id="userCheck"></span></td>
                            </div>
                        </tr>
                        <tr>
                            <div >
                                <td><label for="password_s">Passwort</label></td>
                                <td><input name="passwort1" onkeyup="checkPassword()" type="password" class="input-field" id="password_s" name="password_s" required /></td>
                            </div>
                        </tr>