import requests
import json
import re
from lxml import etree

url = 'http://hotel.qunar.com/city/beijing_city/dt-12768/?tag=beijing_city#fromDate=2018-09-11&toDate=2018-09-12&q=&from=qunarHotel&fromFocusList=0&filterid=0e2efaf7-926a-4185-82cb-0ce963f46c80_A&showMap=0&qptype=&QHFP=ZSS_A09BBD3F'

headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.23 Safari/537.36'
}

res = requests.get(url,headers= headers)
selector = etree.HTML(res.text)
print(selector.xpath('//*[@id="918261"]/ul/li[2]/h2/a/@href'))