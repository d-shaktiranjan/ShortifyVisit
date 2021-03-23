function showKeyword() {
    var checkbox = document.getElementById("flexSwitchCheckDefault");
    var field = document.getElementById("keyword");

    if (checkbox.checked == true){
        field.style.display = "block";
    } else {
        field.style.display = "none";
    }
}