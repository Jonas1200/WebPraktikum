function confirmDelete_p (event_opl) {
    if ((event_opl.target.tagName.toLowerCase() == 'a') && (event_opl.target.className == "clDelete")) {
    // Klick auf Link zum Löschen
        if (!confirm("Möchten Sie sich wirklich von der Veranstaltung abmelden?")) {
            event_opl.preventDefault();
        }
    // Ihre Ergänzung
    }
}

window.onload = function () {
    let body_o = document.getElementsByTagName('body')[0];
    body_o.addEventListener('click', confirmDelete_p, false);
}

function checkLoginData() {
    var d = document;
    if (!!d.getElementById('password2_s')) {
        return checkEmail() && checkPassword();
    }
    return true;
}

function checkEmail() {
    var d  = document;
    if (!!d.getElementById('password2_s')){
        if (d.getElementById('user_s').value.indexOf("hsnr.de") == -1){
                d.getElementById('userCheck').innerHTML = 'Keine Hochschul Email!';
                d.getElementById('userCheck').style.color = 'red';
                return false;
        } else {
            d.getElementById('userCheck').innerHTML = 'Hochschul Email korrekt!';
            d.getElementById('userCheck').style.color = 'green';
            return true;
        }
    }
        
}

function checkPassword(){
    var l = document.Login;
    var d = document;
    var len = false;
    var mat = false;
    if (l.passwort1.value.length == 0){
        d.getElementById('passwordLength').innerHTML = 'Passwort zu kurz!';
        d.getElementById('passwordLength').style.color = 'red';
        len = false;
    } else if (l.passwort1.value.length < 3){
        d.getElementById('passwordLength').innerHTML = 'Mittlere Sicherheit';
        d.getElementById('passwordLength').style.color = 'orange';
        len = true;
    } else if (l.passwort1.value.length >= 3){
        d.getElementById('passwordLength').innerHTML = 'Hohe Sicherheit';
        d.getElementById('passwordLength').style.color = 'green';
        len = true;
    }
    
    if (l.passwort1.value != l.passwort2.value) {
        d.getElementById('passwordMatch').innerHTML = 'Passwörter stimmen nicht überein!';
        d.getElementById('passwordMatch').style.color = 'red';
        var mat = false;
    } else {
        d.getElementById('passwordMatch').innerHTML = 'Passwörter stimmen überein';
        d.getElementById('passwordMatch').style.color = 'green';
        var mat = true;
    }
    return mat && len;
}