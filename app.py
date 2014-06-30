import pymysql
from importlib import import_module
from werkzeug.wrappers import BaseRequest, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException
from werkzeug.serving import run_simple
from werkzeug.contrib.securecookie import SecureCookie

SECRET_KEY = b'\xfa\xdd\xb8z\xae\xe0}4\x8b\xea'

class Request(BaseRequest):

    def start_session(self):
        self.session = SecureCookie.load_cookie(self, secret_key = SECRET_KEY)

    def set_session(self, session):
        self.session = session

    def get_session(self):
        return self.session

class Wipup(object):

    def __init__(self, config):
        self.mysql = pymysql.connect(config['db_host'], config['db_user'],
                                     config['db_pass'], config['db_name'])
        self.routes = Map([
            Rule('/', endpoint=('static', 'homepage')),
            Rule('/wipup', endpoint=('static', 'homepage')),
            Rule('/about', endpoint=('static', 'about'))
        ])

    def get_response(self, request):
        adapter = self.routes.bind_to_environ(request.environ)
        try:
            endpoint, arguments = adapter.match()
            controller = import_module('wipup.controllers.' + endpoint[0])
            method = getattr(controller, endpoint[1])
            return Response(method(request, **arguments), mimetype = 'text/html')
        except HTTPException as e:
            return e

    def run(self, environ, start_response):
        request = Request(environ)
        request.start_session()
        response = self.get_response(request)
        request.get_session().save_cookie(response)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.run(environ, start_response)

def create(db_host = 'localhost', db_user = 'eadrax', db_pass = 'eadrax',
           db_name = 'eadrax'):
    app = Wipup({
        'db_host': db_host,
        'db_user': db_user,
        'db_pass': db_pass,
        'db_name': db_name
    })
    return app

if __name__ == '__main__':
    app = create()
    run_simple('127.0.0.1', 8080, app, use_debugger=True, use_reloader=True)
