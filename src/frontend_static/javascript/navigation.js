/**
 * Created by sheshank.kodam on 4/15/17.
 */

var baseUrl = "http://52.25.29.73:8080/echopath/location";
var locationsOnlyUrl = baseUrl + "/locationsOnly";
var shorestPathBaseUrl = baseUrl + "/shortestPath";
$(document).ready(function () {
    $("#navigation-alert").hide();
    $(".directionsContainerMain").hide();
    buildDropDown($('#fromNameId'), 'From?');
    buildDropDown($('#toNameId'), 'To?');

});

function buildDropDown (dropDownId, emptyMessage) {
    $.ajax({
        type: "GET",
        url: locationsOnlyUrl,
        success: function(data)
        {
            dropDownId.html('');
            dropDownId.append('<option value="">' + emptyMessage + '</option>');
            var locs = data["locations"];
            locs.forEach(function (loc) {
                dropDownId.append('<option value="' + loc.id + '">' + loc.name + '</option>');
            });
        }
    });
}

$(".goBtn").click(function(){
    var fromObj = document.getElementById("fromNameId");
    var toObj = document.getElementById("toNameId");
    var fromLocText = fromObj.options[fromObj.selectedIndex].text;
    var toLocText = toObj.options[toObj.selectedIndex].text;
    var fromLocId = fromObj.options[fromObj.selectedIndex].value;
    var toLocId = toObj.options[toObj.selectedIndex].value;

    if (isEmpty(fromLocId) && isEmpty(toLocId)) {
        showNavigationAlert("Enter a valid From and To values")
        return
    }

    if (isEmpty(fromLocId)) {
        showNavigationAlert("Enter a valid From value")
        return
    }

    if (isEmpty(toLocId)) {
        showNavigationAlert("Enter a valid To value")
        return
    }

    if (!isEmpty(fromLocId) && !isEmpty(toLocId)) {
        showDirections(fromLocText, toLocText, fromLocId, toLocId)
    }
});

function showNavigationAlert(message) {
    $("#navigation-alert").html(message);
    $("#navigation-alert").fadeTo(5000, 500).slideUp(500, function(){
        $("#navigation-alert").slideUp(500);
    });
}

function isEmpty(value){
  return (value == null || value.length === 0);
}

function createDiv(classesArr) {
    return '<div class="' + classesArr.join(' ') + '">';
}

function closeDiv(){
    return '</div>';
}

function createDivWithContent(classesArr, val) {
    return createDiv(classesArr) + val + closeDiv();
}

function showDirections(fromLocName, toLocName, fromLocId, toLocId) {
    $(".directionsContainerMain").show();
    console.log(fromLocName);
    console.log(toLocName);
    var shortestPathUrl = shorestPathBaseUrl + "?fromID=" + fromLocId + "&toID=" + toLocId;
    $.ajax({
        type: "GET",
        url: shortestPathUrl,
        success: function(data)
        {
            console.log(data);
            console.log(data["totalDistance"]);
            // document.getElementsByClassName("directionsContainer").innerHTML = '<p>html data</p>';
            // $(".directionsContainer").html('<div class="row col-xs-12">From: fromLocName</div><div class="row col-xs-12">To</div>');
            $("#fromLocation").html(fromLocName);
            $("#toLocation").html(toLocName);
            $("#distance").html(data["totalDistance"]);

            // display routes..
            createDiv(["row"]);
            $("#routesId").html(
                createDiv(["row"]) +
                    createDivWithContent(["col-xs-12"], fromLocName) +
                closeDiv()
            );
        }
    });

}