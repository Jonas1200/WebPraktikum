                <form id="idWTForm" action="/submitLoginAbsolvent" name="Login" onsubmit="return checkLoginData();" method="POST">
                    <h2>Absolvent</h2>
                    <hr/>
                        <div>
                            <label for="user_s">Email</label>
                            <input type="email" class="input-field" id="user_s" onkeyup="checkEmail();" name="user_s" required />
                            <span id="userCheck"></span>
                        </div>
                            <div >
                                <label for="password_s">Passwort</label>
                                <input type="password" onkeyup="checkPassword()" class="input-field" id="password_s" name="password_s" required />
                            </div>
