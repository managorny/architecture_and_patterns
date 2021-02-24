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

        # Получаем все данные запроса
        method = env['REQUEST_METHOD']
        request_data = self.get_wsgi_input_data(env)

        query_string = env['QUERY_STRING']
        request_params = self.parse_input_data(query_string)

        # добавляем параметры запросов
        request['method'] = method
        request['data'] = request_data
        request['request_params'] = request_params

        for controller in self.front_controllers:
            controller(request)
            if 'path' in request and 'main' in request:
                path = request['path']

        if path in self.urlpatterns:
            view = self.urlpatterns[path]

            status_code, text = view(request)
            first_response(status_code, [('Content-Type', 'text/html')])
            return [text.encode('utf-8')]
        else:
            # view_404 = self.urlpatterns['404']
            # status_code, text = view_404(request)
            status_code = '404 Not Found'
            first_response(status_code, [('Content-Type', 'text/html')])
            return [b'404 Not Found']

    @staticmethod
    def parse_input_data(data: str):
        """
        :param data: принимает декодированну строку входящих данных в запросе
        :return: возвращает словарь
        """
        result = {}
        if data:
            params = data.split('&')

            for item in params:
                key, value = item.split('=')
                result[key] = value
        return result

    def parse_wsgi_input_data(self, data: bytes):
        """
        :param data: принимает байты данных в запросе
        :return: возвращает словарь
        """
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            result = self.parse_input_data(data_str)
        return result

    def get_wsgi_input_data(self, env):
        """
        :param env: получает данные из запроса, если они есть
        :return: словарь
        """
        content_length_data = env.get('CONTENT_LENGTH')
        if content_length_data:
            content_length = int(content_length_data)
        else:
            content_length = 0
        # content_length = int(content_length_data) if content_length_data else 0
        if content_length > 0:
            data = env['wsgi.input'].read(content_length)
        else:
            data = b''
        # data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
        return self.parse_wsgi_input_data(data)
