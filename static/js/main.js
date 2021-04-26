$(document).ready(function () {
    $('.popup').on('click', function () {
        $('.container').css({
            "display": "block"

        });
        $('.close-popup').on('click', function () {
            $('.container').css({
                "display": "none"
            });
        })
    });
});
