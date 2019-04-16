# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask
# def create_app():
from flask_cors import CORS

from .v1 import bp
# import v1

app = Flask(__name__, static_folder='static')
app.register_blueprint(
    bp,
    # v1.bp
    url_prefix='/v1')
    # return app
cors = CORS(app)

# app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = 'f3cfe9ed8fae309f02079dbf'

if __name__ == '__main__':
    app.run(debug=True)
