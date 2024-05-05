from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Car, News
from .forms import RequestForm, RequestFormExtended
import json
import os
import datetime

# Ваша основная директория проекта
#base_dir = '/var/www/auto_site/Carshipment'
base_dir = 'C:/Users/fortu/OneDrive/Desktop/Сайт автомобили/auto_site/Carshipment'

# Имя подкаталога и имя файла
subdirectory = 'main/Bot'
file_name = 'data.json'

# С использованием os.path.join формируем полный путь к файлу
path = os.path.join(base_dir, subdirectory, file_name)


# Create your views here.
def index(request):
    news = [i for i in News.objects.all()]
    news.reverse()
    return render(request, 'main/main.html', {'news': news[:4]})


def setup(request):
    return render(request, 'main/classification.html')


def catalog(request):
    cars = Car.objects.all()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            comment = form.cleaned_data['comment']

            # Проверка пустых полей
            if not name or not phone_number:
                messages.error(request, 'Имя и номер телефона обязательны для заполнения')
            else:
                # Проверка имени на наличие специальных символов и цифр
                if any(char.isdigit() or not char.isalnum() for char in name):
                    messages.error(request, 'Имя не должно содержать специальных символов и цифр')
                # Проверка номера телефона на наличие букв
                elif any(char.isalpha() for char in phone_number):
                    messages.error(request, 'Номер телефона не должен содержать букв')
                else:
                    # Установите значение "Покупка автомобиля" в поле subject
                    form.instance.subject = "Покупка автомобиля"
                    form.instance.date = datetime.datetime.now().date()
                    form.instance.time = datetime.datetime.now().time()
                    form.save()
                    # path = "C:\\Users\\fortu\\OneDrive\\Desktop\\Сайт автомобили\\auto_site\\Carshipment\\main\\Bot\\data.json"

                    # Откройте файл data.json и добавьте новую заявку к существующим данным
                    with open(path, 'r') as json_file:
                        data = json.load(json_file)
                        data.append({
                            'subject': form.instance.subject,
                            'name': form.instance.name,
                            'phone_number': form.instance.phone_number,
                            'date': str(form.instance.date),
                            'time': str(form.instance.time)
                        })

                    # Запишите обновленные данные в файл data.json
                    with open(path, 'w') as json_file:
                        json.dump(data, json_file, indent=4, ensure_ascii=False)

                    messages.success(request, 'Данные успешно отправлены')
                    # Перенаправление на ту же страницу
                    return redirect('/catalog')                            
    else:
        form = RequestForm()

    return render(request, 'main/catalog.html', {'cars': cars, 'form': form})


def model(request):
    car = Car.objects.all()[1]
    return render(request, 'main/model.html', {'car': car, 'images': ['car1.png', 'car2.png', 'cars.png']})


def news(request):
    news = [i for i in News.objects.all()]
    news.reverse()
    return render(request, 'main/news.html', {'news': news})


def contacts(request):
    if request.method == 'POST':
        form = RequestFormExtended(request.POST)
        if form.is_valid():

            form.instance.date = datetime.datetime.now().date()
            form.instance.time = datetime.datetime.now().time()
            form.save()

            # Установите флаг в сессии, чтобы указать успешную отправку формы
            request.session['form_submitted'] = True

            # path = "C:\\Users\\fortu\\OneDrive\\Desktop\\Сайт автомобили\\auto_site\\Carshipment\\main\\Bot\\data.json"

            # Откройте файл data.json и добавьте новую заявку к существующим данным
            with open(path, 'r') as json_file:
                data = json.load(json_file)
                data.append({
                    'subject': form.instance.subject,
                    'name': form.instance.name,
                    'phone_number': form.instance.phone_number,
                    'date': str(form.instance.date),
                    'time': str(form.instance.time)
                })

            # Запишите обновленные данные в файл data.json
            with open(path, 'w') as json_file:
                json.dump(data, json_file, indent=4, ensure_ascii=False)

            # Перенаправление на ту же страницу
            return redirect('/contacts')
    else:
        form = RequestFormExtended()

    # Если форма была успешно отправлена, передайте флаг в контекст
    form_submitted = request.session.get('form_submitted', False)
    request.session['form_submitted'] = False  # Сбросьте флаг после отображения

    return render(request, 'main/contacts.html', {'form': form, 'form_submitted': form_submitted})


def promotion(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            # Установите значение "Покупка автомобиля" в поле subject
            form.instance.subject = "Продажа автомобиля"
            form.instance.date = datetime.datetime.now().date()
            form.instance.time = datetime.datetime.now().time()
            form.save()

            # Установите флаг в сессии, чтобы указать успешную отправку формы
            request.session['form_submitted'] = True

            # path = "C:\\Users\\fortu\\OneDrive\\Desktop\\Сайт автомобили\\auto_site\\Carshipment\\main\\Bot\\data.json"

            # Откройте файл data.json и добавьте новую заявку к существующим данным
            with open(path, 'r') as json_file:
                data = json.load(json_file)
                data.append({
                    'subject': form.instance.subject,
                    'name': form.instance.name,
                    'phone_number': form.instance.phone_number,
                    'date': str(form.instance.date),
                    'time': str(form.instance.time)
                })

            # Запишите обновленные данные в файл data.json
            with open(path, 'w') as json_file:
                json.dump(data, json_file, indent=4, ensure_ascii=False)

            # Перенаправление на ту же страницу
            return redirect('/catalog')
    else:
        form = RequestForm()

    # Если форма была успешно отправлена, передайте флаг в контекст
    form_submitted = request.session.get('form_submitted', False)
    request.session['form_submitted'] = False  # Сбросьте флаг после отображения
    return render(request, 'main/promotion.html', {'form': form, 'form_submitted': form_submitted})
