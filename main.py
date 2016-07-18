# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import os
import time
import re
from selenium import webdriver


def main(ROOT_PATH, link):
    browser = webdriver.Chrome(os.path.join(ROOT_PATH, 'chromedriver'))
    browser.get(link)
    while True:
        time.sleep(4)
        p = browser.find_elements_by_xpath('//*[@id="dUI"]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/a')
        p[0].click()   # start game from title page
        time.sleep(10)
        time.sleep(5)
        fw_id = re.findall(r'\bid="(nhwMiddlegwt-uid-\d+)"', browser.page_source)[0]
        text_id = re.findall(r'\bid="(nhwRightgwt-uid-\d+)"', browser.page_source)[0]
        print(fw_id, text_id)
        time.sleep(10)
        fw = browser.find_element_by_id(fw_id).text
        text = browser.find_element_by_id(text_id).text
        full_text = fw+" "+text
        words = full_text.split(' ')
        for i in words:
            browser.find_element_by_class_name("txtInput").send_keys(i+' ')
            print(i)
            time.sleep(0.9)
        time.sleep(5)
        browser.find_element_by_class_name('raceAgainLink').click()
        browser.refresh()


if __name__ == "__main__":
    ROOT_PATH = os.getcwd()
    link = 'http://play.typeracer.com/'
    main(ROOT_PATH, link)
