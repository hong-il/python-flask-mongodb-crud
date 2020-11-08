/**
 *   @ Author    : hong-il
 *   @ Date      : 2020-11-09
 *   @ File name : header.js
 *   @ File path : /static/assets/js/fragments/header.js
 *   @ Description :
 **/
header = {
    search: function (searchText) {
        let xhr = new XMLHttpRequest();
        xhr.open("GET", "http://127.0.0.1:5000/?search=" + searchText);
        xhr.send();
    }
}

let search = function() {
    const searchText = document.getElementById('searchText').value;

    if (searchText == "")
        return false;
    else
        header.search(searchText);
}