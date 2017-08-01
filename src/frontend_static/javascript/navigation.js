/**
 * Created by sheshank.kodam on 4/15/17.
 */

var locationsUrl = "http://52.25.29.73:8080/echopath/location/locationsOnly";
$(document).ready(function () {
    buildDropDown($('#fromNameId'), 'From?');
    buildDropDown($('#toNameId'), 'To?');

});

function buildDropDown (dropDownId, emptyMessage) {
    $.ajax({
        type: "GET",
        url: locationsUrl,
        success: function(data)
        {
            dropDownId.html('');
            dropDownId.append('<option value="">' + emptyMessage + '</option>');
            var locs = data["locations"];
            var value = 1;
            locs.forEach(function (loc) {
                dropDownId.append('<option value="' + value + '">' + loc.name + '</option>');
                value ++
            });
        }
    });
}