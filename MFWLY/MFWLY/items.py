# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


#此类主要保存某地区内所有景点名字，链接，以及ID
class MfwlyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #地区链接
    url = scrapy.Field()
    #地区ID
    id = scrapy.Field()
    #地区名称
    site = scrapy.Field()
    #pass


#此类主要保存某地区所有景点名称，景点链接
class MfwJDItem(scrapy.Item):
    #景点名字
    name = scrapy.Field()
    #景点链接
    JDurl = scrapy.Field()
    #景点id
    ID = scrapy.Field()

#此类用于保存评论者以及评论内容
class MfwJDcomment(scrapy.Item):
    #评论者
    observer = scrapy.Field()
    #评论
    comment = scrapy.Field()
    #景点ID
    scenicSpotID = scrapy.Field()
