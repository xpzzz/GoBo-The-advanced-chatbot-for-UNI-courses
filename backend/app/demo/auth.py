import logging

from .v1 import bp
from .v1.api import auth


@bp.route('/auth', ['GET'])
def get_access_token():
    logging.info('Called')
    token = auth.get_token()
    return {'token': token}, 200, None

from __future__ import absolute_import

import os
import time

import jwt


def get_token():
    """
    Access-Token Test
    >>> import requests
    >>> token = 'Bearer ' + get_token()
    >>> url = 'https://dialogflow.googleapis.com/v2beta1/projects/gobo-97e5e/agent/sessions/1:detectIntent'
    >>> payload = {"queryInput": {"text": {"text": "hi","languageCode": "en-AU"}}}
    >>> headers = {"Content-Type": "application/json", "Accept": "application/json", "Authorization": token}
    >>> r = requests.post(url, json=payload, headers=headers)
    >>> r.status_code
    200
    """
    SCOPES = ['https://www.googleapis.com/auth/cloud-platform', 'https://www.googleapis.com/auth/dialogflow']

    audience = 'https://dialogflow.googleapis.com/google.cloud.dialogflow.v2beta1.Sessions'

    _kid = os.getenv('GOOGLE_PK_ID')
    _pk = os.getenv('GOOGLE_PK')
    service_account = os.getenv('GOOGLE_SERVICE_ACCOUNT')

    additional_headers = {
        'kid': _kid
    }

    iat = time.time()
    exp = iat + 3600
    payload = {
        'iss': service_account,
        'sub': service_account,
        'aud': audience,
        'exp': exp,
        'iat': iat
    }

    signed_jwt = jwt.encode(payload, _pk, headers=additional_headers, algorithm='RS256')
    # print(payload)
    # print(signed_jwt)
    return signed_jwt.decode('utf-8')


if __name__ == '__main__':
    import doctest

    doctest.testmod()
