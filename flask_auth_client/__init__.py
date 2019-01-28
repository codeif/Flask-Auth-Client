import requests
from requests.auth import HTTPBasicAuth


class AuthClient(object):
    def __init__(self, app=None, base_url=None, username=None, password=None, verify=None):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.verify = verify

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if self.base_url is None:
            self.base_url = app.config['AUTH_CLIENT_BASE_URL']
        if self.username is None:
            self.username = app.config['AUTH_CLIENT_USERNAME']
        if self.password is None:
            self.password = app.config['AUTH_CLIENT_PASSWORD']
        if self.verify is None:
            self.verify = app.config.get('AUTH_CLIENT_VERIFY')

        self.session = requests.Session()
        self.session.auth = HTTPBasicAuth(self.username, self.password)
        if self.verify:
            self.session.verify = self.verify

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
