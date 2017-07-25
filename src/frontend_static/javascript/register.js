/**
 * Created by sheshank.kodam on 4/15/17.
 */
$(document).ready(function () {
    $(".btn_submit").click(function(){
        saveImage();
    });

    function saveImage() {
        console.log("Saving image");
        var firstName = document.getElementsByName("first_name")[0].value;
        var lastName = document.getElementsByName("last_name")[0].value;
        var phoneNumber = document.getElementsByName("phone_number")[0].value;
        var email = document.getElementsByName("email")[0].value;
        var password = document.getElementsByName("password")[0].value;
        var companyName = document.getElementsByName("company_name")[0].value;

        var frm = new FormData();
        frm.append('firstName', firstName);
        frm.append('lastName', lastName);
        frm.append('phoneNumber', phoneNumber);
        frm.append('email', email);
        frm.append('password', password);
        frm.append('companyName', companyName);

        $.ajax({
            type: 'POST',
            url: '/registerUser',
            data: frm,
            contentType: false,
            cache: false,
            processData: false,
            success: function (result) {
               console.log(result);
            },
            error: function (error) {
                console.log(error);
            }
        })
    }
});