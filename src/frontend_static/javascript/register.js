/**
 * Created by sheshank.kodam on 4/15/17.
 */

$(document).ready(function () {
    $("#notification-alert").hide();
    $(".btn_register").click(function(){
        registerUser();
    });
});

function showNotificationAlert(message) {
    $("#notification-alert").html(message);
        $("#notification-alert").fadeTo(5000, 500).slideUp(500, function(){
               $("#notification-alert").slideUp(500);
                });
}

function registerUser() {
    console.log("Saving image");
    var firstName = document.getElementsByName("first_name")[0].value;
    var lastName = document.getElementsByName("last_name")[0].value;
    var phoneNumber = document.getElementsByName("phone_number")[0].value;
    var email = document.getElementsByName("email")[0].value;
    var password = document.getElementsByName("password")[0].value;
    var companyName = document.getElementsByName("company_name")[0].value;
    var gender = document.getElementsByName("gender")[0].value;

    var frm = new FormData();
    frm.append('firstName', firstName);
    frm.append('lastName', lastName);
    frm.append('phoneNumber', phoneNumber);
    frm.append('email', email);
    frm.append('password', password);
    frm.append('companyName', companyName);
    frm.append('gender', gender);

    $.ajax({
        type: 'POST',
        url: '/registerUser',
        data: frm,
        contentType: false,
        cache: false,
        processData: false,
        success: function (result) {
            showNotificationAlert(result)
        },
        error: function (error) {
            showNotificationAlert(error)
        }
    });
}