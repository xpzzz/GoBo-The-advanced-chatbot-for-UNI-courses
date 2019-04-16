# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.auth import Auth
from .api.welcome import Welcome
from .api.ask import Ask
from .api.knowledge_base import KnowledgeBase
from .api.knowledge_base_KID import KnowledgeBaseKid
from .api.knowledge_base_KID_document import KnowledgeBaseKidDocument
from .api.knowledge_base_KID_document_DID import KnowledgeBaseKidDocumentDid


routes = [
    dict(resource=Auth, urls=['/auth'], endpoint='auth'),
    dict(resource=Welcome, urls=['/welcome'], endpoint='welcome'),
    dict(resource=Ask, urls=['/ask'], endpoint='ask'),
    dict(resource=KnowledgeBase, urls=['/knowledge_base'], endpoint='knowledge_base'),
    dict(resource=KnowledgeBaseKid, urls=['/knowledge_base/<KID>'], endpoint='knowledge_base_KID'),
    dict(resource=KnowledgeBaseKidDocument, urls=['/knowledge_base/<KID>/document'], endpoint='knowledge_base_KID_document'),
    dict(resource=KnowledgeBaseKidDocumentDid, urls=['/knowledge_base/<KID>/document/<DID>'], endpoint='knowledge_base_KID_document_DID'),
]