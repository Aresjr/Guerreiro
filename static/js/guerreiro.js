$(document).ready(function() {

    $ajaxView = function ajax(url, callback){
        $.ajax({
            url: url
        }).done(function(response) {
            callback(response);
        }).fail(function(error){
            if(error.status == 401){
                window.location.href = '/login';
            }
        });
    }

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

    $(document).on('input propertychange', 'textarea', function() {
        $(this).css('height', this.scrollHeight+'px');
    });

    $(document).on('click', '.item-menu', function() {
        $('.item-menu').removeClass('active');
        $(this).addClass('active');
    });

    $(document).on('click', '.show-hab', function() {
        const HabId = $(this).data('hab-id');
        $('#hab-filho-'+HabId).toggle({duration: 50});
    });

    $getFormData = function getFormData($form) {
        var unindexed_array = $form.serializeArray();
        var indexed_array = {};
        $.map(unindexed_array, function (n, i) {
            indexed_array[n['name']] = n['value'];
        });
        return indexed_array;
    }

});