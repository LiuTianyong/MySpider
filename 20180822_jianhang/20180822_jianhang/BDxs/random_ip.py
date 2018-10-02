# #coding=utf-8
# import requests
# from scrapy.selector import Selector
# import pymysql
#
# conn = pymysql.connect(host="localhost", user="root", passwd="root", db="scrapyspider", charset="utf8")
# cursor = conn.cursor()
# import  logging
#
#
# class Get_and_validate_id(object):
#
#     #抓取代理IP（西刺网站）
#     def crawl_ips(cursor):
#         headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}
#         for i in range(1568):
#             #直接用request获取网页的资源
#             re = requests.get("http://www.xicidaili.com/nn/{0}".format(i), headers=headers)
#
#             selector = Selector(text=re.text)
#             all_trs = selector.css("#ip_list tr")
#
#
#             ip_list = []
#             for tr in all_trs[1:]:
#                 speed_str = tr.css(".bar::attr(title)").extract()[0]
#                 if speed_str:
#                     speed = float(speed_str.split("秒")[0])
#                 all_texts = tr.css("td::text").extract()
#
#                 ip = all_texts[0]
#                 port = all_texts[1]
#                 proxy_type = all_texts[5]
#                 #看一下打印出来的东西对不对
#                 # print((ip, port, proxy_type, speed))
#                 ip_list.append((ip, port, proxy_type, speed))
#
#
#             #插入数据库
#             for ip_info in ip_list:
#                 cursor.execute(
#                     "insert proxy(ip, port, speed, proxy_type) VALUES('{0}', '{1}', {2}, 'HTTP')".format(
#                         ip_info[0], ip_info[1], ip_info[3]
#                     )
#                 )
#                 conn.commit()
#
#     # 从数据库中删除无效的ip
#     def delete_ip(self, ip):
#         delete_sql = """
#             delete from proxy where ip='{0}'
#         """.format(ip)
#         cursor.execute(delete_sql)
#         conn.commit()
#         return True
#
#     # 判断ip是否可用（直接request from百度，看返回的数据）
#     def judge_ip(self, ip, port):
#         http_url = "http://www.baidu.com"
#         proxy_url = "http://{0}:{1}".format(ip, port)
#         try:
#             proxy_dict = {
#                 "http":proxy_url,
#             }
#             response = requests.get(http_url, proxies=proxy_dict)
#         except Exception as e:
#             print ("invalid ip and port")
#             self.delete_ip(ip)
#             return False
#         else:
#             code = response.status_code
#             if code >= 200 and code < 300:
#                 print ("effective ip")
#                 return True
#             else:
#                 print  ("invalid ip and port")
#                 self.delete_ip(ip)
#                 return False
#
#
#
#
#
# class GetIP(object):
#     #随机获取ip
#     def get_random_ip(self):
#         #从数据库中随机获取一个可用的ip
#         random_sql = """
#               SELECT ip, port FROM proxy
#             ORDER BY RAND()
#             LIMIT 1
#             """
#         result = cursor.execute(random_sql)
#         for ip_info in cursor.fetchall():
#             ip = ip_info[0]
#             port = ip_info[1]
#
#             judge_re = self.judge_ip(ip, port)
#             if judge_re:
#                 return "http://{0}:{1}".format(ip, port)
#             else:
#                 return self.get_random_ip()
#
#
#
# if __name__ == "__main__":
#     Get_and_validate_id()
#     get_ip = GetIP()
#     #用getip方法获取这个ip
#     logging.info('====new round here====')
#     get_ip.get_random_ip()



#coding=utf-8
import requests
from scrapy.selector import Selector
import pymysql
import time
import logging
import re
conn = pymysql.connect(host="localhost", user="root", passwd="root", db="scrapyspider", charset="utf8")
cursor = conn.cursor()

def crawl_ips():
    print('crawl ip process start')
    #爬取西刺的免费ip代理
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5"}
    # for i in range(2000):
    #     #直接用request获取网页的资源
    #     time.sleep(10)
    #     reque = requests.get("http://www.xicidaili.com/nn/{0}".format(i), headers=headers)
    #
    #     selector = Selector(text=reque.text)
    #     all_trs = selector.css("#ip_list tr")
    #
    #     ip_list = []
    #     for tr in all_trs[1:]:
    #         speed_str = tr.css(".bar::attr(title)").extract()[0]
    #         if speed_str:
    #             speed = float(speed_str.split("秒")[0])
    #         all_texts = tr.css("td::text").extract()
    #
    #         ip = all_texts[0]
    #         port = all_texts[1]
    #         proxy_type = all_texts[5]
    #         live = all_texts[-2]
    #         #存活200天以上的ip
    #         if live[-1] == '天':
    #             live = re.sub("\D", "", live)
    #             if int(live) > 200:
    #                 print((ip, port, proxy_type, speed, live))
    #                 ip_list.append((ip, port, proxy_type, speed, live))
    #         else:
    #             continue
    #
    #     #插入数据库
    #     for ip_info in ip_list:
    #         print(ip_info)
    #         cursor.execute(
    #             "insert proxy(ip, port, speed, proxy_type) VALUES('{0}', '{1}', {2}, 'HTTP')".format(
    #                 ip_info[0], ip_info[1], ip_info[3]
    #             )
    #         )
    #         conn.commit()


    # # 西刺不好用，重新找了个代理试一下
    # url_temp = 'http://203.195.167.43/api.asp?key=yinzi210&getnum=1000'
    # re = requests.get(url_temp, headers=headers)
    # selector = Selector(text=re.text)
    #
    # # print('==============================================')
    # all_trs = selector.xpath("//*/text()").extract()
    # all_trs = all_trs[0].split('\r\n')
    # ip_list = []
    # for eve_ip in all_trs:
    #     eve_ip_tem = eve_ip.split(':')
    #     ip_list.append((eve_ip_tem[0],eve_ip_tem[1]))
    # # print(ip_list_temp)
    #
    # #插入数据库
    # for ip_info in ip_list:
    #     cursor.execute(
    #         "insert proxy(ip, port, speed, proxy_type) VALUES('{0}', '{1}', '0', 'HTTP')".format(
    #             ip_info[0], ip_info[1]
    #         )
    #     )

    # conn.commit()
    # print('crawl ip process stoped')

    # # 89代理
    url_temp = []
    for i in range(1, 20):
        url_temp.append('http://www.89ip.cn/index_' + str(i) + '.html')
    url_list = []
    for url in url_temp:
        re = requests.get(url, headers=headers)
        selector = Selector(text=re.text)

        ip_list = selector.xpath('//table[@class="layui-table"]/tbody/tr/td[1]/text()').extract()
        host_list = selector.xpath('//table[@class="layui-table"]/tbody/tr/td[2]/text()').extract()

        all_list = []
        for index, val in enumerate(ip_list):
            all_list.append((val.strip(), host_list[index].strip()))
            url_list.append((val.strip(), host_list[index].strip()))
        for ip_info in all_list:
            cursor.execute(
                "insert proxy(ip, port, speed, proxy_type) VALUES('{0}', '{1}', '0', 'HTTP')".format(
                    ip_info[0], ip_info[1]
                )
            )
            conn.commit()
    return url_list
    print('crawl ip process stoped')


class GetIP(object):
    def delete_ip(self, ip):
        #从数据库中删除无效的ip
        delete_sql = """
            delete from proxy where ip='{0}'
        """.format(ip)
        cursor.execute(delete_sql)
        conn.commit()
        return True

    def judge_ip(self, ip, port):
        #判断ip是否可用
        http_url = "http://www.baidu.com"
        proxy_url = "http://{0}:{1}".format(ip, port)
        try:
            proxy_dict = {
                "http":proxy_url,
            }
            print(proxy_dict)
            response = requests.get(http_url, proxies=proxy_dict)
        except Exception as e:
            print ("invalid ip and port")
            self.delete_ip(ip)
            return False
        else:
            code = response.status_code
            if code >= 200 and code < 300:
                print ("effective ip")
                return True
            else:
                print  ("invalid ip and port")
                self.delete_ip(ip)
                return False


    def get_random_ip(self):
        #从数据库中随机获取一个可用的ip
        random_sql = """
              SELECT ip, port FROM proxy
            ORDER BY RAND()
            LIMIT 1
            """
        result = cursor.execute(random_sql)
        for ip_info in cursor.fetchall():
            ip = ip_info[0]
            port = ip_info[1]

            judge_re = self.judge_ip(ip, port)

            if judge_re:
                return "http://{0}:{1}".format(ip, port)
            else:
                return self.get_random_ip()

    def bianli_ip(self):
        # 从数据库中读取所有的
        allip_sql = """
                      SELECT ip, port FROM proxy
                    ORDER BY RAND()
                    """
        result = cursor.execute(allip_sql)

        for ip_info in cursor.fetchall():
            ip = ip_info[0]
            port = ip_info[1]

            judge_re = self.judge_ip(ip, port)
            return self.bianli_ip()

            # if judge_re:
            #     return "http://{0}:{1}".format(ip, port)
            #
            # else:
            #     return self.bianli_ip()



# crawl_ips()
if __name__ == "__main__":
    get_ip = GetIP()
    #先遍历一遍数据库，去除不可用的ip
    get_ip.bianli_ip()
    # 再随机选择一个ip
    get_ip.get_random_ip()


