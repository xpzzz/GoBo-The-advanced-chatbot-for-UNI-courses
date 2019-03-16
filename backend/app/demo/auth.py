from .v1.api import auth
from . import app


@app.route('/auth', ['GET'])
def get_access_token():
    token = auth.get_token()
    return {'token': token}, 200, None
