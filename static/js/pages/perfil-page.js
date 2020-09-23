$(document).ready(function() {

    ToxProgress.create();
    ToxProgress.animate();

    $(document).on('click', '.show-hab', function () {
        const HabId = $(this).data('hab-id');
        $('#hab-filho-' + HabId).toggle({duration: 50});
    });

});