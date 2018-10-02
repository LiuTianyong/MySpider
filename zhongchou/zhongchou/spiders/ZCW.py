# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ZcwSpider(CrawlSpider):
    name = 'ZCW'
    allowed_domains = ['www.zhongchou.cn']
    start_urls = ['http://www.zhongchou.cn/browse/re-p{}'.format(i) for i in range(1,10)]

    def parse_item(self, response):
        urls = response.xpath('//*[@id="ng-app"]/body/div[6]/div/div/a/@href')
        print(urls)
        #i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
