import requests
from lxml import etree
import random
import csv
import re
from multiprocessing import Pool


fp = open('新闻.csv','wt',newline='',encoding='utf-8')
f = open('新闻.txt','wt',encoding='utf-8')
writer = csv.writer(fp)
writer.writerow(('新闻标题','时间','内容'))
USER_AGENTS = [
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)',
    'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
    'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
    'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
    'Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M032 Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13'
]

def get_list(url):
    headers = {
        'User-Agent': random.choice(USER_AGENTS)
    }
    urls = ['http://www.chinanews.com/scroll-news/news{}.html?'.format(i) for i in range(1,11)]
    for url in urls:
        res = requests.get(url,headers=headers)
        selector = etree.HTML(res.text)
        urls = selector.xpath('//*[@id="content_right"]/div[3]/ul/li/div[2]/a/@href')
        print(urls)
        for url in urls:
            get_comment('http:'+url)

def get_comment(url):
    headers = {
        'User-Agent': random.choice(USER_AGENTS)
    }
    res = requests.get(url,headers=headers)
    res.encoding='gb2312'
    selector = etree.HTML(res.text)
    title = selector.xpath('//*[@id="cont_1_1_2"]/h1/text()')
    time = selector.xpath('//*[@id="cont_1_1_2"]/div[4]/div[2]/text()')
    comments = selector.xpath('//*[@id="cont_1_1_2"]/div[6]/p/text()')
    comment = ''
    for i in comments:
        comment += i
    print(title,time,comment)
    writer.writerow((title,time,comment))
    f.write(str(title))
    f.write(str(time))
    f.write(str(comment))

def get_urls(url):
    headers = {
        'User-Agent': random.choice(USER_AGENTS)
    }
    res = requests.get(url,headers=headers)
    links = ['http://' + res.url + '/cns/s/channel:gj.shtml?&pagenum=400']
    for link in links:
        res = requests.get(link,headers=headers)
        urls = re.findall('"url" : "(.*?)"',res.text,re.S)
        for url in urls:
            get_comment(url)
if __name__ == '__main__':
    urls = [
          'http://www.chinanews.com/scroll-news/news1.html',
          'http://www.chinanews.com/china/',
          'http://world.chinanews.com/',
          'http://mil.chinanews.com/',
          'http://www.chinanews.com/society/',
          'http://finance.chinanews.com/',
          'http://house.chinanews.com/',
          'http://fortune.chinanews.com/',
          'http://www.chinanews.com/stock/gd.shtml',
          'http://www.chinanews.com/gangao/',
          'http://www.chinanews.com/taiwan/',
          'http://www.chinaqw.com/',
          'http://www.chinaqw.com/gqqj/',
          'http://www.chinanews.com/huaren/',
          'http://www.chinanews.com/hb/',
          'http://www.chinaqw.com/hwjy/',
          'http://www.chinanews.com/shipin/',
          'http://www.chinanews.com/shipin/zxft/view.shtml',
          'http://photo.chinanews.com/',
          'http://ent.chinanews.com/',
          'http://sports.chinanews.com/',
          'http://cul.chinanews.com/',
          'http://www.chinanews.com/df/',
          'http://auto.chinanews.com/',
          'http://it.chinanews.com/',
          'http://energy.chinanews.com/',
          'http://health.chinanews.com/',
          'http://life.chinanews.com/',
          'http://wine.chinanews.com/',
          ]
    mydict = {
                'http://www.chinanews.com/scroll-news/news1.html':'滚动',
                'http://www.chinanews.com/china/':'时政',
                'http://world.chinanews.com/':'国际',
                'http://mil.chinanews.com/':'军事',
                'http://www.chinanews.com/society/':'社会',
                'http://finance.chinanews.com/':'财经',
                'http://house.chinanews.com/':'房产',
                'http://fortune.chinanews.com/':'金融',
                'http://www.chinanews.com/stock/gd.shtml':'证券',
                'http://www.chinanews.com/gangao/':'港澳',
                'http://www.chinanews.com/taiwan/':'台湾',
                'http://www.chinaqw.com/':'侨网',
                'http://www.chinaqw.com/gqqj/':'侨界',
                'http://www.chinanews.com/huaren/':'华人',
                'http://www.chinanews.com/hb/':'华报',
                'http://www.chinaqw.com/hwjy/':'华教',
                'http://www.chinanews.com/shipin/':'视频',
                'http://www.chinanews.com/shipin/zxft/view.shtml':'访谈',
                'http://photo.chinanews.com/':'图片',
                'http://ent.chinanews.com/':'娱乐',
                'http://sports.chinanews.com/':'体育',
                'http://cul.chinanews.com/':'文化',
                'http://www.chinanews.com/df/':'地方',
                'http://auto.chinanews.com/':'汽车',
                'http://it.chinanews.com/':'IT',
                'http://energy.chinanews.com/':'能源',
                'http://health.chinanews.com/':'健康',
                'http://life.chinanews.com/':'生活',
                'http://wine.chinanews.com/':'葡萄酒'
}
    for url in urls:
        writer.writerow(mydict[url])
        if url == 'http://www.chinanews.com/scroll-news/news1.html' or 'http://mil.chinanews.com/':
            pool = Pool(processes=4)
            pool.map(get_list,url)
        else:
            pool = Pool(processes=4)
            pool.map(get_urls, url)

    f.close()
    fp.close()