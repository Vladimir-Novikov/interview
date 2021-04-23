// $(document).ready(function () {
//     console.log('after')
//     $('.button').on('click', function () {
//         $.get('/ajax_test/', function (data) {
//             $('#table').html(data);
//             alert('load');
//         })
//     })
// })



$(document).ready(function () {
    $('.button').on('click', function () {
        $.get('/add/', function (data) {
            $('.modal').html(data);
            // $('#table').html(data);
            // $('#modal').style.display = 'block';
            // alert('load');
        })
    })
})