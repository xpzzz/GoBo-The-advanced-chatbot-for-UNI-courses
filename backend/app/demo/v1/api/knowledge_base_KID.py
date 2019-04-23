# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class KnowledgeBaseKid(Resource):

    def get(self, KID):

        return {'id': 'something', 'knowledge-base-name': 'something', 'document-amount': 9573}, 200, None

    def delete(self, KID):

        return None, 200, None