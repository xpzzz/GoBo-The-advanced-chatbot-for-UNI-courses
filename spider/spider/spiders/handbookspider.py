# -*- coding: utf-8 -*-
import scrapy


class HandbookspiderSpider(scrapy.Spider):
    name = 'handbookspider'
    allowed_domains = ['https://www.handbook.unsw.edu.au/postgraduate/courses/2019/COMP9021']
    start_urls = ['https://www.handbook.unsw.edu.au/postgraduate/courses/2019/COMP9021/']

    def parse(self, response):
        for item in response.xpath('//div[@role="main"]'):
            yield {
                'info': item.css('div#subject-intro').css('p::text').getall(),
                'course-name': item.css('div#subject-intro').css('h2').css('span::text').get(),
                'course-code': item.css('div#subject-intro').css('strong.code::text').get(),
                'uoc': item.css('div#subject-intro').css('h4.no-margin.units').css('strong::text').get(),
                'outline': item.css('div#subject-outline').css('a::attr(href)').get()
            }
