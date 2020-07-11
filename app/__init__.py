from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.event_controller import api as event_ns
from .main.controller.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='LBD3',
          version='1.0',
          description='API para o Projeto de Laboratório de Banco de Dados 3 - Calendário estudantil',
          authorizations={
              'Login_Token': {
                  'type': 'apiKey',
                  'in': 'header',
                  'name': 'Authorization'
              }
          },
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(event_ns, path='/event')
api.add_namespace(auth_ns)
