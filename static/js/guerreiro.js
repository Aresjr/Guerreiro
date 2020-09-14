$(document).ready(function() {

  // Scroll to top button appear
  $(document).on('scroll', function() {
    var scrollDistance = $(this).scrollTop();
    if (scrollDistance > 100) {
      $('.scroll-to-top').fadeIn();
    } else {
      $('.scroll-to-top').fadeOut();
    }
  });

  // Smooth scrolling using jQuery easing
  $(document).on('click', 'a.scroll-to-top', function(e) {
    var $anchor = $(this);
    $('html, body').stop().animate({
      scrollTop: ($($anchor.attr('href')).offset().top)
    }, 1000, 'easeInOutExpo');
    e.preventDefault();
  });

    $getFormData = function getFormData($form) {
        var unindexed_array = $form.serializeArray();
        var indexed_array = {};
        $.map(unindexed_array, function (n, i) {
            indexed_array[n['name']] = n['value'];
        });
        return indexed_array;
    }

    $(document).on('input propertychange', 'textarea', function() {
        console.log(this.scrollHeight);
        $(this).css('height', this.scrollHeight+'px');
    });

    $(document).on('click', '.item-menu', function() {
        $('.item-menu').removeClass('active');
        $(this).addClass('active');
    });

    $(document).on('click', '.show-hab', function() {
        const HabId = $(this).data('hab-id');
        $('#hab-filho-'+HabId).toggle('fast');
    });

});