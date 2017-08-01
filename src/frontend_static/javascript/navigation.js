/**
 * Created by sheshank.kodam on 4/15/17.
 */

var locationsUrl = "http://52.25.29.73:8080/echopath/location/locationsOnly";
$(document).ready(function () {
    $.ajax({
        type: "GET",
        url: locationsUrl,
        success: function(data)
        {
            buildDropdown(data, $('#fromNameId'), 'From?');
        }
    });
});

function buildDropdown (result, dropdown, emptyMessage) {
    dropdown.html('');
    dropdown.append('<option value="">' + emptyMessage + '</option>');
    var locs = result["locations"];
    var value = 1;
    locs.forEach(function (loc) {
        dropdown.append('<option value="' + value + '">' + loc.name + '</option>');
        value ++
    });
}