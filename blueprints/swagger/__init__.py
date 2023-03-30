from flask import Blueprint
from flask_restx import Api
from blueprints.swagger.page import namespace as namespace

blueprint = Blueprint('swagger', __name__, url_prefix='/swagger')

api_extension = Api(
    blueprint,
    title='Тайный Санта',
    version='1.0',
    description='Документация к RESTFul API сервису для игры в Тайного Санту.',
    doc='/doc'
)

api_extension.add_namespace(namespace)