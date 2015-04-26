# -*- coding: utf-8 -*-

import httplib
import functools

from flask import (
    jsonify,
    Blueprint,
)

from soya.utils.exc import (
    APIError,
    UpperServiceException,
)


bp = Blueprint('soya', __name__)


def init(app):
    app.register_blueprint(bp, url_prefix='/api')


@bp.route('/ping', methods=['GET'])
def ping():
    return 'ok'


def make_response(data='', code=200, message='ok', status_code=None):
    response = jsonify({
        'code': code,
        'message': message,
        'data': data,
    })

    response.status_code = status_code or httplib.OK
    return response


def render_json(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        return make_response(data)
    return wrapper


@bp.errorhandler(APIError)
def api_error_handler(e):
    return make_response(code=e.code, message=e.message)


@bp.errorhandler(UpperServiceException)
def upper_service_error_handler(e):
    return make_response(code=1000, message=e.message)


from soya.apps.api import (  # noqa
    base,
    amuse,
    assist,
)
