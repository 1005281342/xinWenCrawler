from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup

liuLanQi = webdriver.PhantomJS()
liuLanQi.get('http://news.xnu.edu.cn/article.aspx?ID=124')
jieXi = BeautifulSoup(liuLanQi.page_source, 'lxml')
liuLanQi.maximize_window() #设置全屏
sleep(1)

# xwText = ''
xwFile = open('wenBen', 'w')
xwTextFind = jieXi.select('#form1 > div.contant > div.myright')
# print(xwTextFind[0].get_text())
# xwText = xwText + xwTextFind[0].get_text()
# print(xwText)
hh = xwTextFind[0].get_text().replace('首页>>校园新闻>>', '')
xwFile.write(hh)
print('第1篇已写入文本')
n = 1
while(n < 10000):
    n = n + 1
    try:
        liuLanQi.find_element_by_link_text('上一篇').click()
        sleep(1)
        jieXi = BeautifulSoup(liuLanQi.page_source, 'lxml')
        xwTextFind = jieXi.select('#form1 > div.contant > div.myright')
        # print(xwTextFind[0].get_text())
        # xwText = xwText + xwTextFind[0].get_text()
        hh = xwTextFind[0].get_text().replace('首页>>校园新闻>>', '')
        xwFile.write(hh)
        # print(xwText)
        print("第" + str(n) + '篇已写入文本')
    except:
        print('抓取完成')
        break

xwFile.close()
# print(xwText)
liuLanQi.quit()
