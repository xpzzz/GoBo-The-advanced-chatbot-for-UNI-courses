# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import os

from flask import g, make_response, jsonify, session

from . import Resource
from .implement import bot_manager

_pid = os.getenv('PROJECT_ID')
_allowed_contexts = ['comp9311', 'comp9321']


class Ask(Resource):

    def post(self):
        print(g.json)
        try:
            sid = g.json['sessionID']
            text = g.json['text']
            context = g.json["context"]
            assert (context in _allowed_contexts)
            # if g.json['context']:
            #     print(g.json["context"], "context in json")
            #
            #     context = g.json['context']
            #     session["context"] = context
            #     print("set new context in session ")
            #     #g.sid.context
            # else:
            #     context = session["context"]
            #     print("with old context",context)
            session["context"] = context
        except KeyError:
            return 'Missing essential payload', 400, None
        except AssertionError:
            msg = {
                'message': 'Unknown context',
                'allowed': _allowed_contexts
            }
            resp = make_response(jsonify(msg), 400, None)
            return resp
        text_dict = bot_manager.manage(_pid, sid, text, context)
        # alternative search context like comp9321, comp9311 to replace global var

        resp = make_response(jsonify(text_dict))
        resp.headers['Content-Type'] = 'application/json'
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
