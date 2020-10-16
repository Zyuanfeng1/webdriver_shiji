import time
import lxml.etree
from fake_useragent import UserAgent
from selenium import webdriver
import requests
from selenium.webdriver.support.ui import WebDriverWait

try:
    browser = webdriver.Chrome()
    browser.get('https://www.shicimingju.com/book/shiji.html')
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="main_left"]/div/div[4]/ul/li[2]/a').click()
    for i in range(130):
        time.sleep(3)
        title = browser.find_element_by_xpath('//*[@id="main_left"]/div[1]/h1').text
        print(title)
        time.sleep(3)
        content = browser.find_element_by_xpath('//*[@id="main_left"]/div[1]/div').text
        print(content)
        with open(f'content{i+1}.txt', 'w+', encoding='utf-8') as f:
            f.write(title + '\n')
            f.write(content)
        if(i==0):
            browser.find_element_by_xpath('//*[@id="main_left"]/div[2]/a[2]/span').click()
        else: browser.find_element_by_xpath('//*[@id="main_left"]/div[2]/a[3]/span').click()




except Exception as e:
    print(e)
finally:
    pass
