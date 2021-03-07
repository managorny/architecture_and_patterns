import sys
import os
from views import main_view, about_view, contact_view, err_view

sys.path.append(os.path.join(os.getcwd(), '..'))
from study_framework.core import Application

urlpatterns = {
    '/': main_view,
    '/about/': about_view,
    '/contact_us/': contact_view
}


def main_controller(request):
    request["main"] = "render"
    if request['path']:
        path = request['path']
        if not request['path'].endswith('/'):
            request['path'] = f'{path}/'
    return request


front_controllers = [
    main_controller,
]

application = Application(urlpatterns, front_controllers)
