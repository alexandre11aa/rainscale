window.onload = function () {

    {% if title_error %}
        var toastError = new bootstrap.Toast(document.getElementById('toast_error'));
        toastError.show();
    {% endif %}

    {% if title_success %}
        var toastSuccess = new bootstrap.Toast(document.getElementById('toast_success'));
        toastSuccess.show();
    {% endif %}
    
}