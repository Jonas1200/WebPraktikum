                        
                            <div >
                                <label for="name_s">Name</label>
                                <input type="text" class="input-field" id="name_s" name="name_s" required />
                            </div>
                        
                        
                            <div >
                                <label for="firstname_s">Vorname</label>
                                <input type="text" class="input-field" id="firstname_s" name="firstname_s" required />
                            </div>
                        
                        
                            <div >
                                <label for="matNr_s">Matrikel Nr.</label>
                                <input type="text" maxlength="7" pattern=".{0}|[0-9]{6,7}" class="input-field" id="matNr_s" name="matNr_s" required />
                            </div>
                        
                        
                            <div >
                                <label for="company_s">Anzahl Begleitpersonen</label>
                                <input type="number" min="0" max="4" class="input-field" id="company_s" name="company_s" required />
                            </div>
                        
                        
                            <div >
                                <label for="theme_s">Thema Abschlussarbeit</label>
                                <input type="text" class="input-field" id="theme_s" name="theme_s" required />
                            </div>
   
                            <div >
                                    <label for="type_s">Art der Abschlussarbeit</label>
                                    <select name="type_s" id="type_s">
                                        <option value="bachelor">Bachelor</option>
                                        <option value="master">Master</option>
                                    </select>
                                
                            </div>