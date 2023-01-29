let toastElList = [].slice.call(document.querySelectorAll('.toast'))
let toastList = toastElList.map(function (toastEl) {
    let option = {
    animation: true,
    autohide: false,
    delay: 5000,
    }
    let bsToast = new bootstrap.Toast(toastEl, option)
    bsToast.show();
})

$("#copyright").text(new Date().getFullYear());


// $("#footer-container .body").hide();
// $("#footer-container .footer-button").click(function () {
//     $(this).next("#footer-container div").slideToggle(400);
//     $(this).toggleClass("expanded")
// });
  