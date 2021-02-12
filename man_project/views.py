import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..'))
from study_framework.templates import render


def main_view(request):
    fc_request = request.get('main')
    context = {
        'page_name': 'Main',
        'page_header': 'Main_page',
    }
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
