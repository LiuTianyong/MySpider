# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Request

class MtSpider(scrapy.Spider):
    name = 'MT'
    #allowed_domains = ['meituan.com']
    start_urls = ['http://www.meituan.com/changecity/']

    def parse(self, response):
        urls = re.findall('<a href="//(.*?)" class="link city ">(.*?)</a>',response.text,re.S)
        for url in urls:
            url = 'http://bj.meituan.com/meishi/api/poi/getPoiList?cityName=%E5%8C%97%E4%BA%AC&cateId=0&areaId=0&sort=&dinnerCountAttrId=&page=1&userId=&uuid=9da675588d4148b4b15d.1533649399.1.0.0&platform=1&partner=126&originUrl=http%3A%2F%2Fbj.meituan.com%2Fmeishi%2F&riskLevel=1&optimusCode=1&_token=eJxtj9tugkAQht9lbyXuAguISS%2BgVoqtHASk2PQC5CAsBwXEStN375rYiyZNJvn%2F%2BeaQmS%2FQ6jGYswjJCDFgSFowB%2BwUTUXAgL6jFYHnRYET8QxjmQH7v0zAmAFRu12A%2BTsrsyKDZfRxIxsKKOEQw6IZRb8eU89hGrcunTaBQ98f5xBGxbRK8v4c1tN9U0Hqu0MO6RH%2F1wGdr1w6T5XcNbxr%2F5uv6S90Q5dnNXXJ6lIWXm8q45OtJhPnsEuSdWoc1I68lqrnXHP8LOpVdFxbuOEDyTuLdupI6qObWbyyXpzllXuKsaaZz0tuG8S2paTOC5ZmWg4jmAzjBZYviksi51OtiY%2FNvKn0LbwaxQltiF%2Fp2JNbGBByFMNdUbbF1V5mhfDEs6654o5edjaHunks1RMraMttaMc4n4zNKKTx22Cqoent%2FRNqtUGKnatR7y5phheGRZLesBxpElx8MsYGH4wymoWiEfG%2BMFGUZbbpyQP4%2FgFxT5Lf'
            yield Request(url,)


