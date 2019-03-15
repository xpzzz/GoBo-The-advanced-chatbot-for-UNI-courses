from __future__ import absolute_import

import json

from google.auth import jwt

SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
SERVICE_ACCOUNT_FILE = "/Users/shawn/Documents/2019s1/comp9900/backend/gobo-97e5e-3b2420f2743d.json"
SCOPES_2 = ['https://www.googleapis.com/auth/dialogflow']

# credentials = service_account.Credentials.from_service_account_file(
#         SERVICE_ACCOUNT_FILE, scopes=SCOPES_2)
# print(credentials.__dict__)


service_account_info = json.load(open('./gobo-97e5e-3b2420f2743d.json'))
audience='http://gobo.cfapps.io'
payload = {'data': {'token': 'payload'}}
credentials = jwt.Credentials.from_service_account_info(
    service_account_info,
    audience=audience,
    additional_claims=payload
)
credentials.refresh('')
token = credentials.__dict__['token']
print(token)
print(token.decode('utf-8'))
print(credentials.valid)