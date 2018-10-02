# -*- coding: utf-8 -*-
import scrapy


class TaobaospiderSpider(scrapy.Spider):
    name = 'taobaoSpider'
    allowed_domains = ['taobao.com']
    start_urls = ['http://taobao.com/']

    def parse(self, response):
        pass
