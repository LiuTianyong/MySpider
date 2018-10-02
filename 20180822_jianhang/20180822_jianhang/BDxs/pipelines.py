# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BdxsPipeline(object):
    def process_item(self, item, spider):
        return item


import json
import codecs
#以Json的形式存储
class JsonWithEncodingBDxsPipeline(object):
    def __init__(self):
        self.file = codecs.open('bdxs.json', 'w', encoding='gbk')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()

#将数据存储到mysql数据库
from twisted.enterprise import adbapi
import pymysql
#import MySQLdb
#import MySQLdb.cursors
class MySQLStorePipeline(object):
    #数据库参数
    def __init__(self):
        dbargs = dict(
             host = 'localhost',
             db = 'scrapyspider',
             user = 'root',
             passwd = 'root',
             cursorclass = pymysql.cursors.DictCursor,
             charset = 'utf8',
             use_unicode = True
            )
        self.dbpool = adbapi.ConnectionPool('pymysql',**dbargs)


    '''
    The default pipeline invoke function
    '''
    def process_item(self, item,spider):
        # print('================================pricess start================================')
        res = self.dbpool.runInteraction(self.insert_into_table,item)
        return item
        # print('================================pricess start================================')


    #插入的表，此表需要事先建好
    def insert_into_table(self,conn,item):
        # print('================================pricess start================================')
        conn.execute('insert into jianhang(title,money) values(%s,%s)', (
            item['title'],
            item['money'])
            )
        # print('=================================process finished===============================')