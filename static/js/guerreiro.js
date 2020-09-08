$(document).ready(function() {

    $getFormData = function getFormData($form) {
        var unindexed_array = $form.serializeArray();
        var indexed_array = {};
        $.map(unindexed_array, function (n, i) {
            indexed_array[n['name']] = n['value'];
        });
        return indexed_array;
    }

    $('textarea').bind('input propertychange', function() {
        console.log(this.scrollHeight);
        $(this).css('height', this.scrollHeight+'px');
    });

});