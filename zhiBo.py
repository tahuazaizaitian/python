# -*- coding: UTF-8 -*-
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
browser = webdriver.Chrome(chrome_options=options)

browser.get('http://www.zhibo8.cc/zhibo/nba/2017/052498177.htm')#手动输入直播吧地址

a = browser.find_element_by_xpath('//*[@id="livebox"]/li[1]/div[2]')
b = a
while 1:
    try:
        a = browser.find_element_by_xpath('//*[@id="livebox"]/li[1]/div[2]')
        if b != a.text:
            print a.text,browser.find_element_by_xpath('//*[@id="livebox"]/li[1]/div[3]').text, browser.find_element_by_xpath('//*[@id="livebox"]/li[2]/div[4]').text
            b = a.text
    except:
        hehe = 0
