from __future__ import absolute_import

import json
import time
from os.path import dirname

import jwt
from google.oauth2 import service_account


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

    # NOTE: Don't include this json file in git!
    # Replace it with ur service account credential
    KEY_PATH = dirname(__file__) + '/gobo-97e5e-266614f772e0.json'
    service_account_info = json.load(open(KEY_PATH))
    audience = 'https://dialogflow.googleapis.com/google.cloud.dialogflow.v2beta1.Sessions'

    credentials = service_account.Credentials.from_service_account_info(
        service_account_info,
        scopes=SCOPES,
    )
    # print(credentials.__dict__)
    _kid = service_account_info['private_key_id']
    _pk = service_account_info['private_key']

    additional_headers = {
        'kid': _kid
    }

    iat = time.time()
    exp = iat + 3600
    payload = {
        'iss': 'dialogflow-nnhjie@gobo-97e5e.iam.gserviceaccount.com',
        'sub': 'dialogflow-nnhjie@gobo-97e5e.iam.gserviceaccount.com',
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
