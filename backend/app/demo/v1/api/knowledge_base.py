# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class KnowledgeBase(Resource):

    def get(self):

        return [], 200, None

    def post(self):
        print(g.json)

        return {'id': 'something', 'display-name': 'something', 'document-amount': 9573}, 200, None