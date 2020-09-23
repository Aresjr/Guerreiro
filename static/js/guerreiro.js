$(document).ready(function () {

    $ajaxView = function ajax(url, callback) {
        $.ajax({
            url: url
        }).done(function (response) {
            callback(response);
        }).fail(function (error) {
            if (error.status === 401) {
                window.location.href = '/login';
            }
        });
    }

    $(document).on('click', '.item-menu', function () {
        $('.item-menu').removeClass('active');
        $(this).addClass('active');
    });

    // Scroll to top button appear
    $(document).on('scroll', function () {
        var scrollDistance = $(this).scrollTop();
        if (scrollDistance > 100) {
            $('.scroll-to-top').fadeIn();
        } else {
            $('.scroll-to-top').fadeOut();
        }
    });

    // Smooth scrolling using jQuery easing
    $(document).on('click', 'a.scroll-to-top', function (e) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: ($($anchor.attr('href')).offset().top)
        }, 1000, 'easeInOutExpo');
        e.preventDefault();
    });

    $(document).on('input propertychange', 'textarea', function () {
        $(this).css('height', this.scrollHeight + 'px');
    });

    $getFormData = function getFormData(form) {
        var unindexed_array = $(form).serializeArray();
        var indexed_array = {};
        $.map(unindexed_array, function (n, i) {
            indexed_array[n['name']] = n['value'];
        });
        return indexed_array;
    }

    $createCard = function (itemKanban) {
        var cardKanban = document.createElement("div");
        cardKanban.classList.add("kanban-item");
        cardKanban.classList.add("card");
        cardKanban.classList.add("card-stats");
        cardKanban.classList.add("border-left-primary");
        cardKanban.classList.add("shadow");

        var cardHeader = document.createElement("div");
        cardHeader.classList.add("card-header");

        var cardTitle = document.createElement("h5");
        cardTitle.classList.add("card-title");
        cardTitle.style.fontStyle = 'bold';
        cardTitle.innerHTML = itemKanban.title || itemKanban.id;

        var cardCategory = document.createElement("h6");
        cardCategory.classList.add("card-category");
        cardCategory.style.marginBottom = '0';
        cardCategory.innerHTML = itemKanban.descricao;

        var cardFooter = document.createElement("div");
        cardFooter.classList.add("card-footer");

        var cardFooterUser = document.createElement("div");
        cardFooterUser.innerHTML = itemKanban.executor;
        cardFooterUser.style.fontSize = 'small';

        cardHeader.appendChild(cardTitle);
        cardHeader.appendChild(cardCategory);
        cardKanban.appendChild(cardHeader);
        cardFooter.appendChild(cardFooterUser);
        cardKanban.appendChild(cardFooter);
        return cardKanban;
    };

});