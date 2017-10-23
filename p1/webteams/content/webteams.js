function confirmDelete_p (event_opl) {
    if ((event_opl.target.tagName.toLowerCase() == 'a') && (event_opl.target.className == "clDelete")) {
    // Klick auf Link zum Löschen
        if (!confirm("Do you want to continue deleting?")) {
            event_opl.preventDefault();
        }
    // Ihre Ergänzung
    }
}

window.onload = function () {
    let body_o = document.getElementsByTagName('body')[0];
    body_o.addEventListener('click', confirmDelete_p, false);
}