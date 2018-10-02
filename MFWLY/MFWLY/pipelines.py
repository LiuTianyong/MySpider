# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy import log
import random

class MfwlyPipeline(object):
    def __init__(self):
        #119.29.237.14
        #47.106.108.44
        client_ali = pymongo.MongoClient('119.29.237.14', 27017)  # 连接数据库
        client_tx = pymongo.MongoClient('47.106.108.44', 27017)  # 连接数据库
        mydb_ali= client_ali['MFWLYDQ']
        mydb_tx = client_tx['MFWLYDQ']
        #存地区信息
        self.MFWarea_ali = mydb_ali['MFWarea']
        self.MFWarea_tx = mydb_tx['MFWarea']
        #存景点信息
        self.MFWscenicSpot_ali = mydb_ali['MFWscenicSpot']
        self.MFWscenicSpot_tx = mydb_tx['MFWscenicSpot']
        #存景区信息
        self.MFWseniceSpotComment_ali = mydb_ali['MFWseniceSpotComment']
        self.MFWseniceSpotComment_tx = mydb_tx['MFWseniceSpotComment']

    def process_item(self, item, spider):
        nums = [1,2]
        num = random.choice(nums)
        if num == 1:
            try:
                areaData = {
                    '地区名称': item['site'],
                    '地区链接': item['url'],
                    '地区编号': item['id'],
                }
                self.MFWarea_ali.insert_one(areaData)
                log.msg("写入一条地区信息到阿里云数据库!", level=log.DEBUG, spider=spider)
            except:
                pass
            try:
                scenicSpotData = {
                    '景点': item['name'],
                    '景点链接': item['JDurl'],
                    '景点编号': item['ID'],
                }
                self.MFWscenicSpot_ali.insert_one(scenicSpotData)
                log.msg("写入一条景点到阿里云数据库!", level=log.DEBUG, spider=spider)
            except:
                pass
            try:
                scenicSpotCommentData = {
                    '景点编号': item['scenicSpotID'],
                    '景点评论': item['comment'],
                    '评论者': item['observer']
                }
                self.MFWseniceSpotComment_ali.insert_one(scenicSpotCommentData)
                log.msg("写入一条景点评论阿里云数据库!", level=log.DEBUG, spider=spider)
            except:
                pass
        else:
            try:
                areaData = {
                    '地区名称': item['site'],
                    '地区链接': item['url'],
                    '地区编号': item['id'],
                }
                self.MFWarea_tx.insert_one(areaData)
                log.msg("写入一条地区信息腾讯云数据库!", level=log.DEBUG, spider=spider)
            except:
                pass
            try:
                scenicSpotData = {
                    '景点': item['name'],
                    '景点链接': item['JDurl'],
                    '景点编号': item['ID'],
                }
                self.MFWscenicSpot_tx.insert_one(scenicSpotData)
                log.msg("写入一条景点腾讯云数据库!", level=log.DEBUG, spider=spider)
            except:
                pass
            try:
                scenicSpotCommentData = {
                    '景点编号': item['scenicSpotID'],
                    '景点评论': item['comment'],
                    '评论者': item['observer']
                }
                self.MFWseniceSpotComment_tx.insert_one(scenicSpotCommentData)
                log.msg("写入一条景点评论腾讯云数据库!", level=log.DEBUG, spider=spider)
            except:
                pass
        return item




