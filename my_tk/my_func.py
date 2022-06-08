#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/8/25 18:06
# Author :A0025-江苏-小丹
# QQ:915155536
# File :my_func.py
#  ===========================
import os
import json


# 注册功能
def register():
    while True:
        user_name = input('请输入你要注册的用户名 >>>').strip()
        password = input('请输入你的密码 >>>').strip()
        sec_password = input('请确认你的密码 >>>').strip()
        if password == sec_password:
            # 用户数据文件存放文件
            user_path = f'user_data/{user_name}.json'
            # 判断该用户是否存在
            if os.path.exists(user_path):
                print('该用户已存在，请重新输入！')
                continue
            else:
                # 拼接用户数据
                user_info = {
                    'username': user_name,
                    'password': password
                }
                with open(user_path, 'w', encoding='utf-8') as f:
                    json.dump(user_info, f, ensure_ascii=False)
                    print(f'恭喜你，注册成功！你的用户名为：{user_name},密码为：{password}')
                    break
        else:
            print('两次输入的密码不一致，请重新输入！')
            continue


# 登录功能
def login():
    while True:
        user_name = input('请输入你的用户名 >>>').strip()
        password = input('请输入你的密码 >>>').strip()
        sec_password = input('请确认你的密码 >>>').strip()
        if password == sec_password:
            pass
            # 检查用户是否存在
            user_path = f'user_data/{user_name}.json'
            if os.path.exists(user_path):
                with open(user_path, 'r', encoding='utf-8') as f:
                    d = json.load(f)
                    if d['password'] == password:
                        print('恭喜你，登录成功！')
                        break
                    else:
                        print('sorry,密码错误！再试一次吧！')
                        continue
            else:
                print('您输入的用户不存在，请重新输入！')
                continue
        else:
            print('您两次输入的密码不一致，请重新登录！')
            continue


if __name__ == '__main__':
    register()
    login()
