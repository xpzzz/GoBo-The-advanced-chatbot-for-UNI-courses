import pprint

import scrapy


class HandbookSpider(scrapy.Spider):
    name = 'handbookspider'
    start_urls = ['https://www.handbook.unsw.edu.au/postgraduate/courses/2019/COMP9021/']

    def parse(self, response):
        for item in response.css('div#subject-intro'):
            yield {'text': item.css('p').get()}


if __name__ == '__main__':
    hsp = HandbookSpider()
    hsp.parse()
