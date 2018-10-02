from selenium import webdriver
import time
import requests
from lxml import etree
import re

#景点信息
scenic_spot_message = {}
#评论
comment = []

#提取地方的链接
def info(start):
    start = 'http://www.mafengwo.cn/search/s.php?q=海南'
    res = requests.get(start)
    selector = etree.HTML(res.text)
    href = selector.xpath('//*[@id="_j_search_result_left"]/div[1]/div[1]/h2/a/@href')
    url_1 = re.search('\d+',href[0]).group()
    #http://www.mafengwo.cn/travel-scenic-spot/mafengwo/12938.html
    #http://www.mafengwo.cn/jd/12938/gonglve.html
    url_start = 'http://www.mafengwo.cn/jd/{}/gonglve.html'
    url_jd = url_start.format(url_1)
    info_s(url_jd)

#提取TOP5链接
def info_s(url):
    res =requests.get(url)
    selector = etree.HTML(res.text)
    href = selector.xpath('//*[@id="container"]/div[2]/div/div/div/div/h3/a[1]/@href')
    urls = []
    for url_ in href:
        urls.append('http://www.mafengwo.cn'+url_)
    ##http://www.mafengwo.cn/poi/1667.html
    info_url(urls)

    #爬取信息函数
def info_url(urls):
    #打开谷歌浏览器
    # 测试阶段用谷歌浏览器
    # 爬取时候用无UI界面的PhantomJS浏览器
    driver = webdriver.Chrome()
    #窗口最大化driver.maximize_window()

    for url in urls:
        driver.get(url)
        #隐式等待20秒
        driver.implicitly_wait(20)
        #点击好评
        B = True
        #/html/body/div[3]/div[1]/div/div[3]/div/span
        #景点名称
        try:
            scenic_spot = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[1]/div/h1').text
        except:
            scenic_spot = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[3]/h1').text

        try:
            driver.find_element_by_xpath('//*[@id="comment_header"]/div[4]/div[1]/div[1]/ul/li[1]/div[2]/span').click()
        except:
            B = False

        if B:
            continue
            #A类网页  评论 1 2 3 4 5 等级
            #五星好评  上述已经点过五星好评  这里直接进入爬取函数
            five_star_num = driver.find_element_by_xpath('//*[@id="comment_header"]/div[4]/div[1]/div[1]/ul/li[1]/span').text
            spider(driver)
            #暂时存进字典
            scenic_spot ={
                'five_star_num':five_star_num,
                'five_star_comment':comment,
            }
            #列表清空
            comment = []

            #点击四星好评
            four_star_num = driver.find_element_by_xpath('//*[@id="comment_header"]/div[4]/div[1]/div[1]/ul/li[2]/span').text
            driver.find_element_by_xpath('//*[@id="comment_header"]/div[4]/div[1]/div[1]/ul/li[2]/div[2]/span').click()
            spider(driver)
            scenic_spot = {
                'four_star_num': four_star_num,
                'four_star_comment': comment,
            }
            # 列表清空
            comment = []
            #点击三星
            three_star_num = driver.find_element_by_xpath('//*[@id="comment_header"]/div[4]/div[1]/div[1]/ul/li[3]/span').text
            driver.find_element_by_xpath('//*[@id="comment_header"]/div[4]/div[1]/div[1]/ul/li[3]/div[2]/span').click()
            spider(driver)
            scenic_spot = {
                'three_star_num': three_star_num,
                'three_star_comment': comment,
            }
            # 列表清空
            comment = []
            #点击二星
            two_star_num = driver.find_element_by_xpath('//*[@id="comment_header"]/div[4]/div[1]/div[1]/ul/li[4]/span').text
            driver.find_element_by_xpath('//*[@id="comment_header"]/div[4]/div[1]/div[1]/ul/li[4]/div[2]/span').click()
            spider(driver)
            scenic_spot = {
                'two_star_num': two_star_num,
                'two_star_comment': comment,
            }
            # 列表清空
            comment = []
            #点击一星
            one_star_num =driver.find_element_by_xpath('//*[@id="comment_header"]/div[4]/div[1]/div[1]/ul/li[5]/span').text
            driver.find_element_by_xpath('//*[@id="comment_header"]/div[4]/div[1]/div[1]/ul/li[5]/div[2]/span').click()
            spider(driver)
            scenic_spot = {
                'one_star_num': one_star_num,
                'one_star_comment': comment,
            }
            # 列表清空
            comment = []
        else:
            #B类网页 评论 好 中 差 等级
            #点击锋锋点评
            #driver.find_element_by_xpath('//*[@id="poi-navbar"]/ul/li[3]/a/span').click()
            driver.find_element_by_xpath('//*[@class="r-nav"]/ul/li[3]/a').click()
            #点击好评
            #driver.find_element_by_xpath('//*[@class="review-nav"]/ul/li[3]/a/span').click()
            spiderTWO(driver)

def spider(driver):
    for i in range(1,16):
        comment_ = driver.find_element_by_xpath('//*[@class="_j_commentlist"]/div[{}]/div[2]/div/div[1]/p'.format(i)).text
        comment.append(comment_)
        time.sleep(0.5)

    try:
        driver.find_element_by_link_text("Next>>").click()
    except:
        return

    driver.implicitly_wait(1)
    spider(driver)

def spiderTWO(driver):
    for i in range(1,16):
        time.sleep(5)
        comment_ = driver.find_element_by_xpath('//*[@class="_j_commentlist"]/div[1]/ul/li[{}]/p'.format(i)).text
        #comment.append(comment_)

        print(comment_)
    js = "var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    driver.implicitly_wait(5)
    time.sleep(5)
    driver.find_element_by_link_text('后一页').click()
    spiderTWO(driver)

if __name__ == '__main__':
    start = 'http://www.mafengwo.cn/search/s.php?q=海南'
    info(start)


