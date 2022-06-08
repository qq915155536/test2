#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/4/20 16:46
# Author :黄丹丹
# QQ:915155536
# File :joke_request2.py
#  ===========================

import requests



# 2.拍拍贷
base_headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
}

url = 'https://passport.ppdai.com/api/passport/codeService/webSms?appid=1000002866'
# params={'mobile':'15557195251'}
params = {
    'mobile': 18983212555,
    'callback': 'jQuery11110481999382197849_1646529884149',
    'terminal': 'eed7868cda31ee3fcc53f930239475e9',
    '_': 1646529884151
}
data={
    "extraInfo": {
        "CookieValue": "",
        "FlashValue": "",
        "FpCode": "",
        "_ppdaiWaterMark": "",
        "FromUrl": "",
        "UniqueId": "",
        "UserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
        "sourceId": None,
        "serial_no": "065564d7-f66b-4675-afd2-018a77c9bd4c",
        "currentUrl": "https://account.ppdai.com/pc/login",
        "ppdSearchEngineUrl": None,
        "ImgValidateCode": "",
        "ImgValidateToken": ""
    },
    "type": 1,
    "phone": "HPFRyEMiHQ0n70cHlaY2n2BFZajCcsbYhkQPSQ6Z9kf+z+eyyp31DfqUyudaiwMLQZ42xXiR/0IjniuEQPi1sCIMYYyolIP10DDPDGES9dyW/ie02H1yAqjwKhUjHmSWUsoc7obES691DvuiYgFbAhoc4P77vuftqnmQ629TYn8="
}
res = requests.post(url=url, json=data, headers=base_headers)
print(res.text)
