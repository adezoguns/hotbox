
$(document).ready(function () {

    $('.page-scroll').click(function (event) {

        var anchor = $(this);
        var href = $(anchor).attr('href');

        if (href.substring(0, 1) === '#') {

            $('html, body').stop().animate({
                scrollTop: $(href).offset().top - 130
            }, 1500, 'easeInOutExpo', function () {

            });

            event.preventDefault();
        }
    });

});
