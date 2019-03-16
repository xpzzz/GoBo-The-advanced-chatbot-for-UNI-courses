# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import logging

from flask import request, g

from . import Resource
from .. import schemas

import os
import time

import jwt


class Auth(Resource):

    def get(self):
        print('[ENV] Google Service Account: ' + os.getenv('GOOGLE_SERVICE_ACCOUNT'))
        token = self.get_token()
        return {'token': token}, 200, None

    @staticmethod
    def get_token():

        """
        Access-Token Test
        >>> import requests
        >>> token = 'Bearer ' + self.get_token()
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
