# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class BdxsSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class BdxsDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


from selenium import webdriver
from scrapy.http import HtmlResponse
import time
#
# js = """
#假如有可执行的js程序，需要把函数写在这个地方
# function scrollToBottom() {
#     ....
# }
# scrollToBottom()
# """

class BDxsMiddleware(object):
    #通过chrome请求动态网页
    def process_request(self,request,spider):
        # 设置无头模式
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        # driver = webdriver.Chrome()
        driver.get(request.url)
        time.sleep(3)
        if "enable_redirect" in request.meta.keys():
            driver.find_element_by_xpath('//span[@id="next_span"]/a[@class="page_btn"]').click()
            print("访问：{0}".format(request.url))
            time.sleep(3)
            content = driver.page_source.encode('utf-8')
            return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)
        else:
            print("访问：{0}".format(request.url))
            return HtmlResponse(url=driver.current_url, body=driver.page_source, encoding='utf-8', request=request)





        # if spider.name == 'bdxs':
        #print('===========================跑到这儿啦啦啦啦=======================================')
            # #新建一个浏览器
            # broswer = webdriver.Chrome()
            # #传入请求页面
            # broswer.get(request.url)
            # time.sleep(5)
            # print("访问：{0}".format(request.url))
            #
            # #Htmlresponse用来接收新的URL生成response,然后再parse主函数的Response里面传入这个url
            # return HtmlResponse(url=broswer.current_url,body=broswer.page_source,encoding='utf-8',request=request)


import scrapy
from scrapy import signals
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import random



class MyUserAgentMiddleware(UserAgentMiddleware):
    '''
    设置User-Agent
    '''

    def __init__(self, user_agent):
        self.user_agent = user_agent

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            user_agent=crawler.settings.get('MY_USER_AGENT')
        )

    def process_request(self, request, spider):
        agent = random.choice(self.user_agent)
        request.headers['User-Agent'] = agent





from BDxs.random_ip import GetIP

class RandomProxyMiddleware(object):
    #动态设置ip代理
    def process_request(self, request, spider):
        get_ip = GetIP()
        request.meta["proxy"] = get_ip.get_random_ip()


