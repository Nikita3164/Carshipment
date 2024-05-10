let form = document.querySelector("form");
let form_id = form.id;
let url = "/" + form_id;

form.addEventListener("submit", function(event) {
    event.preventDefault(); // Предотвращаем отправку формы по умолчанию
    
    let flag = true;
    let messageElement = document.getElementById("message");
    let formData = new FormData(form);
    // Получаем все элементы с классом "formField"
    let inputValues = document.getElementsByClassName("formField");

    // Проверяем каждое поле на наличие специальных символов
    for (let i = 0; i < (inputValues.length - 1); i++) {
        let inputValue = inputValues[i].value;
        let regex1 = /[!@#$%^&*(),.?":{}|<>]/; // Регулярное выражение для специальных символов
        let regex2 = /\d/;

        if (regex1.test(inputValue)) {
            // Если найдены специальные символы, выводим сообщение об ошибке
            messageElement.innerText = "Поле не должно содержать специальных символов!";
            messageElement.classList.remove('msg_hidden');
            messageElement.classList.remove('msg_success');
            messageElement.classList.add('msg_error');
            flag = false;
        } else if (regex2.test(inputValue)){
            messageElement.innerText = "Поле не должно содержать цифр!";
            messageElement.classList.remove('msg_hidden');
            messageElement.classList.remove('msg_success');
            messageElement.classList.add('msg_error');
            flag = false; 
        }
        break
        } 

        if (flag){
            // Отправляем AJAX-запрос на сервер Django
            $.ajax({
                url: url,  // Замените на URL вашей Django-функции
                type: "POST",
                data: formData,
                contentType: false,
                processData: false,
                success: function(response) {
                    // Обработка успешного ответа от сервера первого запроса
                    console.log('Успех!');
                    document.getElementById("message").innerText = "Заявка успешно отправлена!";
                    document.getElementById("message").classList.remove('msg_hidden');
                    messageElement.classList.remove('msg_error');
                    messageElement.classList.add('msg_success');
            
                    // Здесь выполняется второй AJAX-запрос
                    $.ajax({
                        url: url, // URL вашей Django-функции для получения данных
                        type: 'GET',
                        dataType: 'json',
                        success: function(response) {
                            // Обработка успешного ответа от сервера второго запроса
                            console.log('Успех второго запроса!');
                            console.log(response);
                        },
                        error: function(xhr, status, error) {
                            // Обработка ошибки второго запроса
                            console.error('Ошибка второго запроса:', error);
                        }
                    });
                },
            
                error: function(xhr, status, error) {
                    // Обработка ошибки
                    console.error(xhr.responseText);
                }
            })}});