$(".menu-title i").click(function () {
   $(this).parent().parent().next().toggleClass('hides');
    if ($(this).hasClass('fa-plus')){
        $(this).removeClass('fa-plus');
        $(this).addClass('fa-minus');
    }else {
        $(this).removeClass('fa-minus');
        $(this).addClass('fa-plus');

    }
});

$(window).scroll(function () {
        if ($(window).scrollTop() < 500 ){
            $('#back-to-top').addClass('hides');
        } else {
            $('#back-to-top').removeClass('hides');
        }
});

$('#back-to-top').click(function () {
    $(window).scrollTop(0);
});

