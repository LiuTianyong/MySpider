# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from MFWLY.items import MfwlyItem,MfwJDItem,MfwJDcomment
import re
from scrapy import Request
from scrapy import FormRequest
import json
import requests


class MfwSpider(CrawlSpider):
    name = 'MFW'
    allowed_domains = ['mafengwo.cn']
    start_urls = ['http://www.mafengwo.cn/mdd/']

    #匹配到所有有景点的地区URL
    rules = (
        Rule(LinkExtractor(allow=r'http://www.mafengwo.cn/travel-scenic-spot/mafengwo/\d+.html'), callback='parse_item', follow=True),
    )

    num = 2
    def parse_item(self, response):
        item = MfwlyItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        item['url'] = response.url
        item['id'] = re.findall('\d+',item['url'])[0]
        item['site'] = response.xpath('.//*[@class="title"]/h1').extract()[0]
        yield item

        #地区页面请求头
        headers = {
            'Host': 'www.mafengwo.cn',
            'Origin': 'http://www.mafengwo.cn',
            'Referer': 'http://www.mafengwo.cn/jd/{}/gonglve.html/'.format(item['id']),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

        url = 'http://www.mafengwo.cn/ajax/router.php'
        #页码初始量
        page = 1
        while True:
            yield FormRequest(
                url,
                callback= self.parse_url,
                method='POST',
                headers=headers,
                formdata={
                    'sAct': 'KMdd_StructWebAjax|GetPoisByTag',
                    'iMddid': str(item['id']),
                    'iTagId': '0',
                    'iPage': str(page)
                    }
                )
            page += 1
            if page > self.num:
                break

    def parse_url(self ,response):
        url_header = 'http://www.mafengwo.cn'
        item = MfwJDItem()
        temporary = json.loads(response.text)
        temporaryText = temporary['data']['list']
        temporaryText_ = temporary['data']['page']
        #该景点名称
        scenicSpots = re.findall('<h3>(.*?)</h3>', temporaryText)
        #该景点的链接
        url_ends = re.findall('<a href="(.*?)"', temporaryText)


        #JD_id = re.findall()
        # #该地区景点总页数
        self.num = re.findall('<a class="pi pg-last" data-page="(.*?)"',temporaryText_,re.S)[0]

        for url_end,scenicSpot in zip(url_ends,scenicSpots):
            item['name'] = scenicSpot
            item['JDurl'] = url_header + url_end
            #该景点ID
            JD_id = re.findall('\d+',url_end)[0]
            item['ID'] = JD_id
            yield item

            page = 0
            #请求评论区
            url_ = 'http://pagelet.mafengwo.cn//poi/pagelet/poiCommentListApi?params={%22poi_id%22:%22'+str(item['ID'])+'%22,%22page%22:'
            url_e = ',%22just_comment%22:1}'
            url  = url_ + '1' + url_e
            a = requests.get(url)
            v = a.json()
            h = v['data']['html']
            num = re.findall('<a class="pi pg-last" data-page="(.*?)"',h)[0]
            num = int(num)
            while True:
                if page <= num:
                    page += 1
                    url = url_ + str(page) +url_e
                    yield Request(url, callback=self.scenicSpotComment)
                else:
                    break


    def scenicSpotComment(self,response):
        item = MfwJDcomment()
        temporary = json.loads(response.text)
        temporaryText = temporary['data']['html']

        #评论
        comments = re.findall('<p class="rev-txt">(.*?)</p>',temporaryText)
        observers = re.findall('data-comment_username="(.*?)"',temporaryText)
        scenicSpotIDs = re.findall('href="/u/(.*?).html"',temporaryText)

        for observer,comment,scenicSpotID in zip(observers,comments,scenicSpotIDs):
            item['comment'] = comment
            item['observer'] = observer
            item['scenicSpotID'] = scenicSpotID
            yield item









