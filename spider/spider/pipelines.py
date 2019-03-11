# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from pprint import pprint
import logging


class SpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class HandbookNormalisePipeline(object):

    def process_item(self, item, spider):
        _tmp = item['intro']
        intro = ''
        for _ in _tmp:
            intro += f'{_}'
            # 去掉\n 因为是一个整体intent：intro
        intro.replace('\u00a0', ' ').rstrip('\n')
        intro = '"'+intro+'"'
        #左右添加""使,不分割csv文件
        #TODO CSV : 后换行

        item['intro'] = intro
        logging.debug(f'Now item is: {intro}')

        for k, v in item.items():
            if isinstance(v, list):
                item[k] = v[0]
        return item


class CSVWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('handbook.csv', 'w',encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        for k, v in item.items():
            line = f'{k},{str(v)}\n'
            logging.debug(f'{type(v)}')
            logging.debug(f'Going to write {line}')
            self.file.write(line)
        return item
