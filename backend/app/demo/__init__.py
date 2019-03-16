# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask



# def create_app():
from .v1 import bp

app = Flask(__name__, static_folder='static')
app.register_blueprint(
    bp,
    url_prefix='/v1')
    # return app


if __name__ == '__main__':
    app.run(debug=True)
