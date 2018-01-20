function confirmDelete_p (event_opl) {
    if ((event_opl.target.tagName.toLowerCase() == 'a') && (event_opl.target.className == "clDelete")) {
    // Klick auf Link zum Löschen
        if (!confirm("Möchten Sie wirklich fortfahren?")) {
            event_opl.preventDefault();
        }
    // Ihre Ergänzung
    }
}
document.addEventListener("DOMContentLoaded", presetPruefer);

window.onload = function () {
    let body_o = document.getElementsByTagName('body')[0];
    body_o.addEventListener('click', confirmDelete_p, false);
    if (document.getElementById("pruefer1") != null) {
        var pruefer1 = document.getElementById("pruefer1");
        pruefer1.addEventListener("change", pruefer1Change, false);
        var pruefer2 = document.getElementById("pruefer2");
        pruefer2.addEventListener("change", pruefer2Change, false);

    }
}



function presetPruefer(){
    d = document;
    if (pruefer1 = d.getElementById('pruefer1') != null){
        pruefer1 = d.getElementById('pruefer1');
        pruefer2 = d.getElementById('pruefer2');
        if (pruefer1.className != "empty"){
            var str = 'f' + pruefer1.className;
            console.log(str);
            d.getElementById(str).selected = true;
            strpruefer2 = 's' + pruefer1.className;
            console.log(strpruefer2);
            if (d.getElementById(strpruefer2) != null){
                d.getElementById(strpruefer2).style.display = "none";
            }
        } else{
            d.getElementById("empty1").selected = true;
        }
        if (pruefer2.className != "empty"){
            var str = 's' + pruefer2.className;
            d.getElementById(str).selected = true;
            strpruefer1 = 'f' + pruefer2.className;
            console.log(strpruefer1);
            if (d.getElementById(strpruefer1) != null){
                d.getElementById(strpruefer1).style.display = "none";
            }
        } else{
            d.getElementById("empty2").selected = true;
        }
    }
}

function pruefer1Change (event_opl) {
    var d = document
    //pruefer1 = d.getElementById('pruefer1');
    console.log(this.value + "has been selected");
    var sel = d.getElementById("pruefer2");
    for (i = 0; i < sel.options.length; i++)
    {
        sel[i].style.display = "";
    }
    var idStr = 's' + this.value;
    var opt = d.getElementById(idStr);
    opt.style.display = "none";
}

function pruefer2Change (event_opl) {
    var d = document
    console.log(this.value + "has been selected");
    var sel = d.getElementById("pruefer1");
    for (i = 0; i < sel.options.length; i++)
    {
        sel[i].style.display = "";
    }
    var idStr = 'f' + this.value;
    var opt = d.getElementById(idStr);
    opt.style.display = "none";
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
    if (l.password_s.value.length == 0){
        d.getElementById('passwordLength').innerHTML = 'Passwort zu kurz!';
        d.getElementById('passwordLength').style.color = 'red';
        len = false;
    } else if (l.password_s.value.length < 3){
        d.getElementById('passwordLength').innerHTML = 'Mittlere Sicherheit';
        d.getElementById('passwordLength').style.color = 'orange';
        len = true;
    } else if (l.password_s.value.length >= 3){
        d.getElementById('passwordLength').innerHTML = 'Hohe Sicherheit';
        d.getElementById('passwordLength').style.color = 'green';
        len = true;
    }
    
    if (l.password_s.value != l.password2_s.value) {
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