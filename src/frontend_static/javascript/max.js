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

        var frm = new FormData();
        frm.append('firstName', firstName);
        frm.append('lastName', lastName);

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