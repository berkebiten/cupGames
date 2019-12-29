document.getElementById("defaultOpen").click();

function tab(evt, leaderboarName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(leaderboarName).style.display = "block";
    evt.currentTarget.className += " active";
}

function login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if (username == "user" && password == "password") {
        window.location.href = 'HomepageUser.html';
    } else if (username == "admin" && password == "password") {
        window.location.href = 'HomepageAdmin.html';
    } else if (username == "premium" && password == "password") {
        window.location.href = 'HomepagePremium.html';
    } else {
        alert("Wrong username or password");
    }
}

function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function (event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}


function checkFunc(checkId) { // check all checkboxes when checked ALL
    var inputs = document.getElementsByTagName("input");
    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].type === "checkbox" && inputs[i].id === checkId) {
            if (inputs[i].checked === true) {
                inputs[i].checked = false;
            } else if (inputs[i].checked === false) {
                inputs[i].checked = true;
            }
        }
    }
}