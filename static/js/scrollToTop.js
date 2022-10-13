$('.btt-link').click(() => {
    window.scrollTo(0, 0)
})

$(window).scroll(function () {
    if ($(document).scrollTop() > 100) {
        $('.btt-link').css('opacity', 1)
    } else {
        $('.btt-link').css('opacity', 0)
    }
});

$('.btt-link').css('opacity', 0)