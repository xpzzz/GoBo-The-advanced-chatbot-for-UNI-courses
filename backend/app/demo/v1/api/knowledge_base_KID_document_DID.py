# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class KnowledgeBaseKidDocumentDid(Resource):

    def get(self, KID, DID):

        return {'display-name': 'something', 'MIME-type': 'something', 'Knowledge-type': 'something'}, 200, None

    def delete(self, KID, DID):

        return None, 200, None