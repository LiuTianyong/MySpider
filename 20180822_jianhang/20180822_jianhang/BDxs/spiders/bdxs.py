# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import  Request
from urllib import parse
from BDxs.items import BdxsItem
import time
from selenium import webdriver

class BdxsSpider(scrapy.Spider):
    # 配置driver路径，问题：为什么直接加入到path里面不行啊？
    # driver = webdriver.Chrome()

    name = 'bdxs'
    allowed_domains = ['finance.ccb.com']
    start_urls = ['http://finance.ccb.com/cn/finance/product.html']

    # paper_num = 0
    page_num = 0


    def parse(self, response):

        jianhang_temp_list = []
        title_list = response.xpath('//td[@class="list_title"]/div/div/a/@title').extract()
        money_list = response.xpath('//div[@class="pro_tab pro_tab1 clearfix"]/table/tbody/tr/td[2]').extract()

        for index,val in enumerate(title_list):
            jianhang_temp_list.append((val,str(money_list[index]).replace('<td>','').replace('</td>','')))
        for item in jianhang_temp_list:
            jianhang = BdxsItem()
            jianhang['title'] = item[0]
            jianhang['money'] = item[1]
            yield jianhang

        # 获取下一页url
        request = Request(url=response.url, callback=self.parse)
        request.meta['enable_redirect'] = True
        yield request

        #打印一轮的文章数还有页面数
        print('page_num='+str(self.page_num))
        # print('paper_num='+str(self.paper_num))






