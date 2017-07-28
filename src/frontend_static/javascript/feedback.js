/**
 * Created by sheshank.kodam on 4/15/17.
 */
$(document).ready(function () {
    $("#feedback-alert").hide();
    $(".btn_submit_feedback").click(function(){
        submitFeedback();
    });
});

function showFeedbackNotification(message) {
    $("#feedback-alert").html(message);
        $("#feedback-alert").fadeTo(5000, 500).slideUp(500, function(){
               $("#feedback-alert").slideUp(500);
                });
}


function submitFeedback() {
    var name = document.getElementsByName("name")[0].value;
    var email = document.getElementsByName("email")[0].value;
    var feedbackText = document.getElementById("subject").value;

    var frm = new FormData();
    frm.append('name', name);
    frm.append('email', email);
    frm.append('feedbackText', feedbackText);

    $.ajax({
        type: 'POST',
        url: '/feedback',
        data: frm,
        contentType: false,
        cache: false,
        processData: false,
        success: function (result) {
            showFeedbackNotification(result)
        },
        error: function (error) {
            showFeedbackNotification(error)
        }
    });
}