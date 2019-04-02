# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from .implement import knowledge_base_implement as imp
import os

_pid = os.getenv('PROJECT_ID')

class KnowledgeBase(Resource):

    def __init__(self):
        assert(os.getenv('PROJECT_ID'))

    def get(self):

        imp.list_knowledge_bases(_pid)
        return [], 200, None

    def post(self):
        print(g.json)

        return {'id': 'something', 'display-name': 'something', 'document-amount': 9573}, 200, None