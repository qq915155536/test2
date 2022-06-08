#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/4/1 14:18
# Author :黄丹丹
# QQ:915155536
# File :1.py
#  ===========================


from selenium import webdriver
# 7 def send_360(phon_num):
#     8     option = webdriver.ChromeOptions()
# 9     option.add_argument('headless')
# 10     browser = webdriver.Chrome(chrome_options=option)
# 11     browser.get('https://www.360jie.com.cn/')

    # options=webdriver.ChromeOptions()
    # options.add_argument('headless')
phone_num1='15557195251'
phone_num2='18983212555'

browser=webdriver.Chrome()
browser.get('https://www.360jie.com.cn/')
browser.maximize_window()
browser.find_element('name','mobile').send_keys(phone_num2)
browser.find_element('id','btnSendCode1').click()



