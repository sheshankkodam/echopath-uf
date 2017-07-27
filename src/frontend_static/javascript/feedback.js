/**
 * Created by sheshank.kodam on 4/15/17.
 */
$(document).ready(function () {
    $("#feedback-alert").hide();
    $(".btn_submit_feedback").click(function(){
        var feedbackText = document.getElementById('feedbackId').value;
        submitFeedback(feedbackText);
    });
});

function showFeedbackNotification(message) {
    $("#feedback-alert").html(message);
        $("#feedback-alert").fadeTo(5000, 500).slideUp(500, function(){
               $("#feedback-alert").slideUp(500);
                });
}


function submitFeedback(text) {
    $.ajax({
        type: 'POST',
        url: '/feedback',
        data: text,
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