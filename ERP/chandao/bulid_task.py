#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/5/9 9:21
# Author :黄丹丹
# QQ:915155536
# File :bulid_task.py  3533
#  ===========================
from selenium import webdriver


num = int(input('麻烦输入，你的需求号 >>>').strip())

browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(10)
url = 'http://121.199.45.21:9000/zentao/my-story.html'
browser.get(url)

# 1.登录禅道
browser.find_element('name', 'account').send_keys('huangdandan')
browser.find_element('name', 'password').send_keys('123456')
browser.find_element('id', 'submit').click()

# 2.寻找需求
browser.find_element('id', 'searchInput').send_keys(num)
browser.find_element('id', 'searchGo').click()

# 3.查看需求或者新增任务
tag = int(input('你的操作 : 1.继续新增任务  2.退出浏览器 >>>').strip())
# tag = 1
if tag != 1:
    browser.quit()
else:

    # 4.新建任务
    # 1）任务名称
    task_name = str(num) + browser.find_element('xpath', '//span[@class="text"]').text + '【测试】'
    print('任务名称：',task_name)
    # 2）点击创建任务
    # <1>滑动滚动条
    js = 'window.scrollBy(0,10000)'
    browser.execute_script(js)
    # <2>刷新页面
    browser.refresh()
    # <3>点击项目任务
    a = browser.find_element('css selector', '#legendProjectAndTask > ul > li:nth-child(1) > a.text-muted')
    if a:
        a.click()
    else:
        print('关联项目未找到！')
    # <4>点击建任务
    browser.find_element('xpath', '//a[@class="btn btn-primary"]').click()
    # <5>选择任务类型
    browser.find_element('id', 'type_chosen').click()
    browser.find_element('xpath', '//li[@title="测试"]').click()
    # <6>选择所属模块
    browser.find_element('id', 'module_chosen').click()
    browser.find_element('xpath', '//li[@title="/"]').click()
    # <7>选择指派人
    browser.find_element('id', 'assignedTo_chosen').click()
    browser.find_element('xpath', '//li[@title="H:黄丹丹"]').click()
    # <8>选择相关需求
    browser.find_element('id', 'story_chosen').click()
    browser.find_element('xpath', '//*[@id="story_chosen"]/a/div[2]/input').send_keys(num)
    browser.find_element('xpath', '//*[@id="story_chosen"]/div/ul/li').click()
    # <9>输入任务名称
    browser.find_element('id', 'name').send_keys(task_name)
    # <10>输入预计工时
    browser.find_element('id', 'estimate').send_keys('8')
    # <11>滑动滚动条
    browser.execute_script(js)
    # <12>点击完成
    browser.find_element('id', 'submit').click()
    print('测试任务，添加成功！')
    browser.quit()
    print('浏览器已退出！')

