$(document).ready(function() {

    $('form.ajax').submit(function (event) {
        event.preventDefault();
    });

    $getFormData = function getFormData($form) {
        var unindexed_array = $form.serializeArray();
        var indexed_array = {};
        $.map(unindexed_array, function (n, i) {
            indexed_array[n['name']] = n['value'];
        });
        return indexed_array;
    }

    $('textarea').bind('input propertychange', function() {
        $(this).css('height', this.scrollHeight+'px');
    })
});