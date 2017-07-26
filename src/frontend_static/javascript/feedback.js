/**
 * Created by sheshank.kodam on 4/15/17.
 */
$(document).ready(function () {
    $("#success-alert").hide();
    $(".btn_submit_feedback").click(function(){
        console.log("submit feedback");
        $("#success-alert").html("Success");
        $("#success-alert").fadeTo(5000, 500).slideUp(500, function(){
               $("#success-alert").slideUp(500);
                });

    });
});