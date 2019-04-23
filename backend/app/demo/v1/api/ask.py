# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

<<<<<<< HEAD
import os

from flask import g, make_response, jsonify, session
from . import Resource
from .implement import bot_manager

_pid = os.getenv('PROJECT_ID')
_allowed_contexts = ['comp9311', 'comp9321']
=======
from flask import request, g, make_response, jsonify, session


from . import Resource
from .. import schemas
from .implement import detect_intent_via_text as di
import os

_pid = os.getenv('PROJECT_ID')
>>>>>>> master


class Ask(Resource):

    def post(self):
        print(g.json)
        try:
            sid = g.json['sessionID']
            text = g.json['text']
            context = g.json["context"]
<<<<<<< HEAD
            assert (context in _allowed_contexts)
=======
>>>>>>> master
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
<<<<<<< HEAD
        except AssertionError:
            msg = {
                'message': 'Unknown context',
                'allowed': _allowed_contexts
            }
            resp = make_response(jsonify(msg), 400, None)
            return resp
        text_dict = bot_manager.manage(_pid, sid, text, context)
        # alternative search context like comp9321, comp9311 to replace global var

=======

        text_dict = di.detect_intent_texts(_pid, sid, text, context)
>>>>>>> master
        resp = make_response(jsonify(text_dict))
        resp.headers['Content-Type'] = 'application/json'
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
