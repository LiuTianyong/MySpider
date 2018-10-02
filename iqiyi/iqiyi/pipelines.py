# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy import log

class IqiyiPipeline(object):
    def __init__(self):
        client_ali = pymongo.MongoClient('119.29.237.14', 27017)  # 连接数据库
        mydb_ali= client_ali['mydb']
        self.MFWarea_ali = mydb_ali['tanmu']

    def process_item(self, item, spider):
        for i,j in zip(item['episodeNum'],item['barrage']):
            doc = {
                '剧集': i,
                '弹幕': j,
            }
            self.MFWarea_ali.insert_one(doc)
        log.msg("写入一条地区信息到阿里云数据库!", level=log.DEBUG, spider=spider)
        return item
