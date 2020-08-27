$(document).ready(function() {
    $('textarea').bind('input propertychange', function() {
        $(this).css('height', this.scrollHeight+'px');
    })
});