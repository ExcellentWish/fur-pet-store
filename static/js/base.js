$(document).ready(function () {
    let toastElList = [].slice.call(document.querySelectorAll('.toast'));
    let toastList = toastElList.map(function (toastEl) {
        let option = {
            animation: true,
            autohide: false,
            delay: 5000,
        };
        let bsToast = new bootstrap.Toast(toastEl, option);
        bsToast.show();
    });

    $("#copyright").text(new Date().getFullYear());



    // quantity_input_script
    // Disable +/- buttons outside 1-99 range
    function handleEnableDisable(itemId) {
        var currentValue = parseInt($(`#id_qty_${itemId}`).val());
        var minusDisabled = currentValue < 2;
        var plusDisabled = currentValue > 98;
        $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
        $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
    }

    // Ensure proper enabling/disabling of all inputs on page load
    var allQtyInputs = $('.qty_input');
    for (var i = 0; i < allQtyInputs.length; i++) {
        var itemId = $(allQtyInputs[i]).data('item_id');
        handleEnableDisable(itemId);
    }

    // Check enable/disable every time the input is changed
    $('.qty_input').change(function () {
        var itemId = $(this).data('item_id');
        handleEnableDisable(itemId);
    });

    // Increment quantity
    $('.increment-qty').click(function (e) {
        e.preventDefault();
        var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
        var currentValue = parseInt($(closestInput).val());
        $(closestInput).val(currentValue + 1);
        var itemId = $(this).data('item_id');
        handleEnableDisable(itemId);
    });

    // Decrement quantity
    $('.decrement-qty').click(function (e) {
        e.preventDefault();
        var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
        var currentValue = parseInt($(closestInput).val());
        $(closestInput).val(currentValue - 1);
        var itemId = $(this).data('item_id');
        handleEnableDisable(itemId);
    });
// For reviews
    function deleteModal() {
        $("#delete-review").on('click', function () {
            $('#confirmationModal').modal('show');
        });

        $(".close").on('click', function () {
            $('#confirmationModal').modal('hide');
        });
    }
    deleteModal();
// for superuser delete
    function deleteProductModal() {
        $("#delete-product-{{ product.id }}").on('click', function () {
            $('#confirmationModal-{{ product.id }}').modal('show');
        });

        $(".close").on('click', function () {
            $('#confirmationModal-{{ product.id }}').modal('hide');
        });
    }
    deleteProductModal();
});