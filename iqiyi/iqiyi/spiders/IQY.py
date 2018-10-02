# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Request
from iqiyi.items import IqiyiItem
import random

class IqySpider(scrapy.Spider):
    name = 'IQY'
    #此处填写改爬取的电视剧 第一集url  或电影url  或其他
    def parse(self, response):
        i  = 3878316
        while True:
            if i > 4878316:
                break
            url = ']    A2yoJygLvKJcSF0d&agenttype=118&wallId=259595647&feedTypes=1%2C7%2C8%2C9&count=20&top=1&hasRecomFeed=1&feedId=94628937748&needTotal=1&notice=1&version=1&upOrDown=1&snsTime=153408{}'.format(random.randrange(2000,5000)) + '&m_device_id=a00d8ba3f45f7a4381b734df0e1d8e25f595cc41a874daa785fd7e7311601295c4&_=153408{}'.format(i)
            yield Request(url= url,callback=self.parse_coment)
            i += 1

    def parse_coment(self,response):
        item = IqiyiItem()
        page = response.text
        #爬取什么改成什么参数
        # type_ = '电视剧'
        # if type_ == '电视剧':
        #     if page['code'] == 'A00000':
        #         comments = page['data']['feeds']
        #         for i in comments:
        #             try:
        #                 temporary = i['baseVideo']['tvTitle']
        #                 num = re.findall('\d+', temporary)[0]
        #                 item['episodeNum'] = num
        #             except:
        #                 pass
        #             comment = i['description']
        #             item['barrage'] = comment
        #             # print('***********测试靓仔***********************')
        comments = re.findall('"description":"(.*?)"', page, re.S)
        nums = re.findall('"tvTitle":"为了你我愿意热爱整个世界第(\d+)集"', page, re.S)
        # for i,j in zip(nums,comments):
        #     item['episodeNum'] = i
        #     item['barrage'] = j
        item['episodeNum'] = comments
        item['barrage'] = nums
        yield item



