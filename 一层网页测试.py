import requests
from lxml import etree
import re

url = 'https://www.iqiyi.com/v_19rqydwy5o.html'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.23 Safari/537.36'
}
res = requests.get(url,headers=headers)
r = re.findall('"wallId":\d+',res.text)[0]
print(r)
s = re.findall('"wallId":(\d+)',r)[0]
print(s)