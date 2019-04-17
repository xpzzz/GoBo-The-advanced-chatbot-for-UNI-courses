import os
from typing import List

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv(verbose=True)
client = MongoClient(os.environ['MONGO_URL'])
db = client[os.environ['MONGO_NAME']]
collection = db['stackoverflow_records']


def insert_document(json: dict):
    if not collection.find_one({'_id': json.get('_id')}):
        collection.insert_one(json)
    else:
        print(f'[DB_DRIVER] {json.get("_id")} skipped')


def update_document(_id, json: dict):
    collection.find_one_and_replace({'_id': _id}, json, upsert=True)


def get_a_document(query: dict):
    collection.find(query)


# def get_documents_for_training() -> List[dict]:
#     count = collection.count({'query_term': 'python'})
#     res = []
#     for i in range(count):
#         json = get_a_document({'query_term': 'python'})
#