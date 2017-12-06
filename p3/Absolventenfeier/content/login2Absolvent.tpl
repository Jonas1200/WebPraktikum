                        <tr>
                            <div >
                                <td><label for="name_s">Name</label></td>
                                <td><input type="text" class="input-field" id="name_s" name="name_s" required /></td>
                            </div>
                        </tr>
                        <tr>
                            <div >
                                <td><label for="firstname_s">Vorname</label></td>
                                <td><input type="text" class="input-field" id="firstname_s" name="firstname_s" required /></td>
                            </div>
                        </tr>
                        <tr>
                            <div >
                                <td><label for="matNr_s">Matrikel Nr.</label></td>
                                <td><input type="text" maxlength="7" pattern=".{0}|[0-9]{6,7}" class="input-field" id="matNr_s" name="matNr_s" required /></td>
                            </div>
                        </tr>
                        <tr>
                            <div >
                                <td><label for="company_s">Anzahl Begleitpersonen</label></td>
                                <td><input type="number" min="0" max="4" class="input-field" id="company_s" name="company_s" required /></td>
                            </div>
                        </tr>
                        <tr>
                            <div >
                                <td><label for="theme_s">Thema Abschlussarbeit</label></td>
                                <td><input type="text" class="input-field" id="theme_s" name="theme_s" required /></td>
                            </div>
                        </tr>
                        <tr>
                            <div >
                                <td><label for="type_s">Art der Abschlussarbeit</label></td>
                                <td>
                                    <select name="type_s" id="type_s">
                                        <option value="bachelor">Bachelor</option>
                                        <option value="master">Master</option>
                                    </select>
                                </td>
                            </div>
                        </tr>