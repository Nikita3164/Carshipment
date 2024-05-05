document.getElementById("myForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Предотвращаем отправку формы по умолчанию
    
    let inputValue = document.getElementsByClassName("myInput").value;
    let regex = /[!@#$%^&*(),.?":{}|<>]/; // Регулярное выражение для специальных символов
    
    if (regex.test(inputValue)) {
        document.getElementById("error-message").innerText = "Поле не должно содержать специальных символов!";
        document.getElementById("error-message").style.display = "block";
    } else {
        // Отправляем AJAX-запрос на сервер Django
        $.ajax({
            url: "post_test_data",  // Замените на URL вашей Django-функции
            type: "POST",
            data: formData,
            contentType: false,
            processData: false,
            success: function(response) {
                // Обработка успешного ответа от сервера
                console.log(response);
            },
            error: function(xhr, status, error) {
                // Обработка ошибки
                console.error(xhr.responseText);
            }
        });
    }
});