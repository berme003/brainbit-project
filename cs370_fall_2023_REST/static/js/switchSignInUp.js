let signupBtn = document.getElementById("signupBtn");
let signinBtn = document.getElementById("signinBtn");
let nameField = document.getElementById("nameField");
let dobField = document.getElementById("dobField");
let genderField = document.getElementById("genderField");

signinBtn.onclick = function () {
    nameField.style.maxHeight = "0";
    dobField.style.maxHeight = "0";
    genderField.style.maxHeight = "0";
    signupBtn.classList.add("disable");
    signinBtn.classList.remove("disable");
}


signupBtn.onclick = function () {
    nameField.style.maxHeight = "100px";
    dobField.style.maxHeight = "100px";
    genderField.style.maxHeight = "100px";
    signupBtn.classList.remove("disable");
    signinBtn.classList.add("disable");
}
