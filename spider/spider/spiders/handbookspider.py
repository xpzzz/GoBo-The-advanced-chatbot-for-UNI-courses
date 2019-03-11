# -*- coding: utf-8 -*-
from __future__ import absolute_import
import scrapy
from scrapy.loader import ItemLoader
from ..items import HandbookItem


class HandbookspiderSpider(scrapy.Spider):
    name = 'handbookspider'
    allowed_domains = ['https://www.handbook.unsw.edu.au/postgraduate/courses/2019/COMP9021']
    start_urls = ['https://www.handbook.unsw.edu.au/postgraduate/courses/2019/COMP9021/']

    def parse(self, response):
        il = ItemLoader(item=HandbookItem(), response=response)
        # il.nested_xpath('//div[@role="main"')
        il.add_xpath('name', '//div[@id="subject-intro"]/h2/span/text()')
        il.add_xpath('code', '//div[@id="subject-intro"]/div/div/h4/strong[@class="code"]/text()')
        il.add_xpath('intro', '//div[@id="subject-intro"]/div/div/p/text()')
        il.add_xpath('uoc', '//div[@id="subject-intro"]/div/div/h4[@class="no-margin units"]/strong/text()')
        il.add_xpath('outline', '//div[@id="subject-outline"]/div/a/@href')

        return il.load_item()
    # yield {
    #     'intro': item.css('div#subject-intro').css('p::text').getall(),
    #     'name': item.css('div#subject-intro').css('h2').css('span::text').get(),
    #     'code': item.css('div#subject-intro').css('strong.code::text').get(),
    #     'uoc': item.css('div#subject-intro').css('h4.no-margin.units').css('strong::text').get(),
    #     'outline': item.css('div#subject-outline').css('a::attr(href)').get()
    # }
