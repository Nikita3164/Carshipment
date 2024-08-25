from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
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


def spam_check(name, text):
    users_blacklist = ['AmandaEffelf']
    words_blacklist = ['Ukraine', 'Украин', 'продвижени', 'полуприцеп', 'базы', 'бота', 'search', 'Search']
    for i in users_blacklist:
        if i in name:
            return True
    for j in words_blacklist:
        if j in text:
            return True
    return False 


def catalog(request):
    cars = Car.objects.all()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid() and not spam_check(form.instance.name, form.instance.comment):
            # Установите значение "Покупка автомобиля" в поле subject
            form.instance.subject = "Покупка автомобиля"
            form.instance.date = datetime.datetime.now().date()
            form.instance.time = datetime.datetime.now().time().strftime('%H:%M')
            form.save()
            #path = "C:\\Users\\fortu\\OneDrive\\Desktop\\Сайт автомобили\\auto_site\\Carshipment\\main\\Bot\\data.json"

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
            
            message = {
                'message': 'Success',
                'status': 'ok'
            }
            return JsonResponse(message)                           
    else:
        form = RequestForm()

    return render(request, 'main/catalog.html', {'cars': cars, 'form': form})


def model(request, id):
    car = get_object_or_404(Car, id=id)
    return render(request, 'main/model.html', {'car': car, 'images': car.img_addresses.split(', ')})


def news(request):
    news = [i for i in News.objects.all()]
    news.reverse()
    return render(request, 'main/news.html', {'news': news})


def contacts(request):
    if request.method == 'POST':
        form = RequestFormExtended(request.POST)
        if form.is_valid() and not spam_check(form.instance.name, form.instance.comment):

            form.instance.date = datetime.datetime.now().date()
            form.instance.time = datetime.datetime.now().time().strftime('%H:%M')
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
            message = {
                'message': 'Success',
                'status': 'ok'
            }
            return JsonResponse(message) 
    else:
        form = RequestFormExtended()

    return render(request, 'main/contacts.html', {'form': form})


def promotion(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid() and not spam_check(form.instance.name, form.instance.comment):
            # Установите значение "Покупка автомобиля" в поле subject
            form.instance.subject = "Продажа автомобиля"
            form.instance.date = datetime.datetime.now().date()
            form.instance.time = datetime.datetime.now().time().strftime('%H:%M')
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
            message = {
                'message': 'Success',
                'status': 'ok'
            }
            return JsonResponse(message) 
    else:
        form = RequestForm()

    return render(request, 'main/promotion.html', {'form': form})


def security(request):
    return render(request, 'main/security.html')


def privacy(request):
    return render(request, 'main/privacy.html')


def agreement(request):
    return render(request, 'main/agreement.html')
