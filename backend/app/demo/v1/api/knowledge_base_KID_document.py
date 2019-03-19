# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class KnowledgeBaseKidDocument(Resource):

    def post(self, KID):
        print(g.json)

        return {'display-name': 'something', 'MIME-type': 'something', 'Knowledge-type': 'something'}, 200, None