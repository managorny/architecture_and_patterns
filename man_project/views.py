import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..'))
from study_framework.templates import render


def main_view(request):
    fc_request = request.get('main')
    context = {
        'page_name': 'Курсы по вождению',
        'page_header': 'Курсы по вождению. Главная',
    }
    if request['method'] == 'GET':
        context['request_params'] = request['request_params']
        context['method'] = request['method']
    return '200 OK', render('index.html', fc_request=fc_request, context=context)


def about_view(request):
    fc_request = request.get('main')
    context = {
        'page_name': 'About',
        'page_header': 'About_page',
    }
    return '200 OK', render('index.html', fc_request=fc_request, context=context)


def err_view(request):
    fc_request = request.get('main')
    context = {
        'page_name': '404',
        'page_header': '404_page',
    }
    return '404 Not Found', render('404.html', fc_request=fc_request, context=context)


def contact_view(request):
    context = {
        'page_name': 'Обратная связь',
        'page_header': 'Обратная связь',
    }
    if request['method'] == 'POST':
        data = request['data']
        title = data['title']
        text = data['text']
        email = data['email']
        with open('messages.txt', 'a') as f:
            f.write(f'Пришло сообщение от {email}. Тема: {title}. Текст: {text}\n')
        print(f'Пришло сообщение от {email}. Тема: {title}. Текст: {text}\n')
        return '200 OK', render('contact_us.html', context=context)
    else:
        return '200 OK', render('contact_us.html', context=context)
