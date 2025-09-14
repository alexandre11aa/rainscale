window.onload = function () {

    if (window.title_error) {
        var toastError = new bootstrap.Toast(document.getElementById('toast_error'));
        toastError.show();
    }

    if (window.title_success) {
        var toastSuccess = new bootstrap.Toast(document.getElementById('toast_success'));
        toastSuccess.show();
    }

};