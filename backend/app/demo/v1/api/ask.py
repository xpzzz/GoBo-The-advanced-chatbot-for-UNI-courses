# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from .implement import detect_intent_via_text as di
import os

_pid = os.getenv('PROJECT_ID')


class Ask(Resource):

    def post(self):
        # print(g.json)
        # print('testing...')
        #
        # print(g.json['text'])
        # print(g.json['sessionID'])
        # print(_pid)
        #
        # print('testing ends....')

        sid = g.json['sessionID']
        text = g.json['text']

        if not sid or not text:
            # TODO this check is not working rn
            return 'Missing essential payload', 401, None

        text_dict = di.detect_intent_texts(_pid, sid, text)

        return text_dict, 200, None
