import requests
from requests.auth import HTTPBasicAuth


class AuthClient(object):

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.base_url = app.config['AUTH_CLIENT_BASE_URL']
        username = app.config['AUTH_CLIENT_USERNAME']
        password = app.config['AUTH_CLIENT_PASSWORD']
        verify = app.config.get('AUTH_CLIENT_VERIFY')

        self.session = requests.Session()
        self.session.auth = HTTPBasicAuth(username, password)
        if verify:
            self.session.verify = verify

    def request(self, method, path, **kwargs):
        url = self.base_url + path
        return self.session.request(method, url, **kwargs)

    def get(self, path, **kwargs):
        return self.request('GET', path, **kwargs)

    def options(self, path, **kwargs):
        return self.request('OPTIONS', path, **kwargs)

    def head(self, path, **kwargs):
        return self.request('HEAD', path, **kwargs)

    def post(self, path, **kwargs):
        return self.request('POST', path, **kwargs)

    def put(self, path, **kwargs):
        return self.request('PUT', path, **kwargs)

    def patch(self, path, **kwargs):
        return self.request('PATCH', path, **kwargs)

    def delete(self, path, **kwargs):
        return self.request('DELETE', path, **kwargs)
