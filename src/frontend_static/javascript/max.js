/**
 * Created by sheshank.kodam on 4/15/17.
 */
$(document).ready(function () {
    console.log("Hello src");

    $(".default_image").click(function(){
        console.log("Clicked on image");
        $('#uploaded_file').trigger('click');
    });

    $("#uploaded_file").change(function(){
        console.log("File upload received");
        previewImage(this);

    });

    $(".btn_submit").click(function(){
        saveImage();
    });



    function previewImage(input) {
        console.log("Previewing image");
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('.default_image').attr('src', e.target.result);
            };
            reader.readAsDataURL(input.files[0]);
        }
    }

    function saveImage() {
        console.log("Saving image");
        var oFiles = document.getElementById("uploaded_file").files;
        var avatar = oFiles[0];
        var firstName = document.getElementsByName("first_name")[0].value;
        var lastName = document.getElementsByName("last_name")[0].value;
        var dateOfBirth = document.getElementsByName("dob")[0].value;

        var frm = new FormData();
        frm.append('avatar', avatar);
        frm.append('firstName', firstName);
        frm.append('lastName', lastName);
        frm.append('dateOfBirth', dateOfBirth);
        console.log("Saving image");
        $.ajax({
            type: 'POST',
            url: '/upload',
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