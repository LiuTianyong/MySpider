# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhongxinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #标题
    title = scrapy.Field()
    #时间
    time = scrapy.Field()
    #内容
    comment = scrapy.Field()
