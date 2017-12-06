                <form id="idWTForm" action="/submitLoginAbsolvent" name="Login" onsubmit="return checkLoginData();" method="POST">
                    <h2>Absolvent</h2>
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
                                <td><input type="password" onkeyup="checkPassword()" class="input-field" id="password_s" name="password_s" required /></td>
                            </div>
                        </tr>