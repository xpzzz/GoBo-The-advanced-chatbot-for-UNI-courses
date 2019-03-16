# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask



# def create_app():
import v1

app = Flask(__name__, static_folder='static')
app.register_blueprint(
    v1.bp,
    url_prefix='/v1')
    # return app


if __name__ == '__main__':
    app.run(debug=True)
