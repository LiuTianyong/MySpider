# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import re
from zhongxin.items import ZhongxinItem
from lxml import etree


class ZxwSpider(scrapy.Spider):
    name = 'zxw'
    start_urls = ['//www.chinanews.com/scroll-news/news1.html',
                '//www.chinanews.com/china/',
                '//world.chinanews.com/',
                '//mil.chinanews.com/',
                '//www.chinanews.com/society/',
                '//finance.chinanews.com/',
                '//house.chinanews.com/',
                '//fortune.chinanews.com/',
                '//www.chinanews.com/stock/gd.shtml',
                '//www.chinanews.com/gangao/',
                '//www.chinanews.com/taiwan/',
                'http://www.chinaqw.com/',
                'http://www.chinaqw.com/gqqj/',
                '//www.chinanews.com/huaren/',
                '//www.chinanews.com/hb/',
                'http://www.chinaqw.com/hwjy/',
                '//www.chinanews.com/shipin/',
                '//www.chinanews.com/shipin/zxft/view.shtml',
                '//photo.chinanews.com/',
                '//ent.chinanews.com/',
                '//sports.chinanews.com/',
                '//cul.chinanews.com/',
                '//www.chinanews.com/df/',
                '//auto.chinanews.com/',
                '//it.chinanews.com/',
                '//energy.chinanews.com/',
                '//health.chinanews.com/',
                '//life.chinanews.com/',
                '//wine.chinanews.com/',
                ]
    start_urls = 'http:'+start_urls[5]
    def parse(self, response):
        print(response.url)
        url = ['http://'+response.url+'/cns/s/channel:gj.shtml?pager={}&pagenum=20'.format(i) for i in range(0,20)]
        yield Request(url,callback=self.get_url)

    def get_url(self,response):
        urls = re.findall('"url" : "(.*?)"',response.text,re.S)
        yield Request(urls,callback=self.get_comment)

    def get_comment(self,response):
        item = ZhongxinItem()
        response.encoding = 'gb2312'
        selector = etree.HTML(response.text)
        item['title'] = selector.xpath('//*[@id="cont_1_1_2"]/h1/text()')
        item['time'] = selector.xpath('//*[@id="cont_1_1_2"]/div[4]/div[2]/text()')
        comments = selector.xpath('//*[@id="cont_1_1_2"]/div[6]/p/text()')
        comment = ''
        for i in comments:
            comment += i
        item['comment'] = comment
        yield item


