var btns = document.getElementsByClassName("nav-link")

console.log(btns);

var path = window.location.pathname;
var page = path.split("/").pop();

console.log(page)

document.addEventListener("DOMContentLoaded", function(e) {
    if (page == "william"){
        btns[1].className = btns[1].className += " active";
    }
    if (page == "map"){
        btns[2].className = btns[2].className += " active";
    }
})
