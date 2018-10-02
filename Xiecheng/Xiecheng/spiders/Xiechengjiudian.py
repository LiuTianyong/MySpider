# -*- coding: utf-8 -*-
import scrapy
from Xiecheng.items import XiechengItem


class XiechengjiudianSpider(scrapy.Spider):
    name = 'Xiechengjiudian'
    base_url = "http://hotels.ctrip.com/hotel/beijing1/p"
    offset = 1
    start_urls = [base_url + str(offset)]

    def parse(self, response):
        info_html = response.xpath("//div[@id='divNoresult']")
        print(response.headers)

        if len(info_html) <= 0:
            node_list = response.xpath("//ul[@class='hotel_item']")

            for node in node_list:
                item = XiechengItem()

                if len(node.xpath(".//h2[@class ='hotel_name']/a/@href")) > 0:
                    item['hotel_url'] = node.xpath('//*[@id="918261"]/ul/li[2]/h2/a/@href').extract()[0]
                    print(item['hotel_url'])
                else:
                    item['hotel_url'] = ''

                if len(node.xpath(".//h2[@class ='hotel_name']/a/text()")) > 0:
                    item["hotel_name"] = node.xpath(".//h2[@class ='hotel_name']/a/text()").extract()[0]

                else:
                    item["hotel_name"] = ""

                if len(node.xpath(".//a/img/@src")) > 0:
                    item["hotel_img"] = node.xpath(".//a/img/@src").extract()[0]
                else:
                    item["hotel_img"] = ""

                if len(node.xpath(".//p[@class='hotel_item_htladdress']/text()")) > 0:
                    str_address = "".join(node.xpath(".//p[@class='hotel_item_htladdress']/text()").extract())
                    if "】" in str_address:
                        str_address = str_address[str_address.index("】") + 1:]
                    item["hotel_address"] = str_address
                else:
                    item["hotel_address"] = ""

                if len(node.xpath(".//span[@class='hotel_value']/text()")) > 0:
                    item["hotel_point"] = node.xpath(".//span[@class='hotel_value']/text()").extract()[0]
                else:
                    item["hotel_point"] = ""

                if len(node.xpath(".//span[@class='hotel_judgement']/span/text()")) > 0:
                    item["hotel_judgement"] = node.xpath(".//span[@class='hotel_judgement']/span/text()").extract()[0]
                else:
                    item["hotel_judgement"] = ""

                if len(node.xpath(".//span[@class='J_price_lowList']/text()")) > 0:
                    item["hotel_price"] = node.xpath(".//span[@class='J_price_lowList']/text()").extract()[0]
                else:
                    item["hotel_price"] = ""
                if len(item['hotel_url']) > 0:
                    yield scrapy.Request('http://hotels.ctrip.com/' + item['hotel_url'],
                                         callback=self.info)
                yield item

            self.offset += 1
            next_url = self.base_url + str(self.offset)
            yield scrapy.Request(next_url, callback=self.parse)
    def info(self, response):
        print(response.text)