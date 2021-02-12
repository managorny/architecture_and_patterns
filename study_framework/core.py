class Application:
    def __init__(self, urlpatterns: dict, front_controllers: list):
        """
        :param urlpatterns: словарь для связи url-view
        :param front_controllers: общие слои для всех urls (Middlewares)
        """
        self.urlpatterns = urlpatterns
        self.front_controllers = front_controllers

    def __call__(self, env, first_response):
        path = env['PATH_INFO']
        request = {'path': path}
        for controller in self.front_controllers:
            controller(request)
            if 'path' in request and 'main' in request:
                path = request['path']

        if path in self.urlpatterns:
            view = self.urlpatterns[path]

            status_code, text = view(request)
            print(status_code, text)
            first_response(status_code, [('Content-Type', 'text/html')])
            return [text.encode('utf-8')]
        else:
            # view_404 = self.urlpatterns['404']
            # status_code, text = view_404(request)
            status_code = '404 Not Found'
            first_response(status_code, [('Content-Type', 'text/html')])
            return [b'404 Not Found']
