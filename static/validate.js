function validateForm() {
    var name = document.forms["contact"]["name"].value;
    var emailAddress = document.forms["contact"]["email"].value;
    var comment = document.forms["contact"]["comment"].value;
    if (name == "") {
        var message = "Please enter your name";
        } else if (emailAddress == "") {
            var message = "Please enter an email address";
        } else if (comment == "") {
            var message = "You didn't leave a comment";
        }
        else {
            var message = "Thank you for your comment"
        }
            alert(message);
            return false;
    }
