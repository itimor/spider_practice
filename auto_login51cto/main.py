# -*- coding: utf-8 -*-
# author: itimor

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

url = 'http://home.51cto.com/index?reback=http://blog.51cto.com'
name = 'jay541430183'
password = 'jay541430183'
search_word = 'python'


# 开始登录
opts = Options()
opts.binary_location = '/data/App/Google Chrome.app/Contents/MacOS/Google Chrome'
driver = webdriver.Chrome(chrome_options=opts)
driver.maximize_window()   #窗口最大化
driver.implicitly_wait(5)
driver.get(url)

elem_account = driver.find_element_by_id("loginform-username")
elem_password = driver.find_element_by_id("loginform-password")

elem_account.clear()
elem_password.clear()
elem_account.send_keys(name)
elem_password.send_keys(password)
print "点击登录"
elem_password.send_keys(Keys.RETURN)

print "进入页面"
elem_search = driver.find_element_by_id("sq")
elem_search.clear()
elem_search.send_keys(search_word)
elem_search.send_keys(Keys.RETURN)

print "打印元素"
elem_articles = driver.find_elements_by_xpath("//h2//a")
for i in elem_articles:
    print i.text

driver.quit()