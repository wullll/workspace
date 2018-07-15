#!/usr//lib/python
# coding=utf-8
from urllib.parse import urljoin
from requests.sessions import Session
from pprint import pprint
import requests
import unittest
"""
接口说明：
登录接口：
请求url ： /login
请求方法： post
请求参数： username String 登录名称
          password String 登录密码
响应信息： code Integer 结果code
          msg  String 结果信息  
详情接口：
请求url： /info
请求方法: get
请求参数： session String session
响应信息： code  Integer 结果code
          msg   String  结果信息
          data  String  数据信息                 

"""


# 封装常用方法
class DemoApi(object):
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = Session()    # 创建session实例

    def login(self, username, password):
        url = urljoin(self.base_url, 'login')
        data = {"username": username, "password": password}
        response = self.session.post(url, data).json()
        print("\n*********************************")
        print("\n1 请求url： \n %s" % url)
        print('\n2 请求头信息：')
        pprint(self.session.headers)
        print('\n3 请求参数：')
        pprint(data)
        print('\n4 响应：')
        pprint(response)
        return response

    def get_cookies(self, username, password):
        url = urljoin(self.base_url, 'login')
        data = {'username': username, 'password': password}
        return requests.post(url, data).cookies

    def info(self):
        url = urljoin(self.base_url, 'info')
        response = self.session.get(url).json()
        print("\n*********************************")
        print("\n1 请求url： \n%s" % url)
        print('\n2 请求头信息：')
        pprint(self.session.headers)
        print('\n3 请求cookie：')
        pprint(dict(self.session.cookies))
        print('\n4 响应：')
        pprint(response)
        return response


# 登录接口测试类
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = 'http://127.0.0.1:5000'
        # cls.login_url = 'http://127.0.0.1:5000/login'
        # cls.info_url = 'http://127.0.0.1:5000/info'
        cls.username = 'admin'
        cls.password = '123456'
        cls.app = DemoApi(cls.base_url)

    # 测试登录接口
    def test_login(self):
        response = self.app.login(self.username, self.password)
        assert response['code'] == 200
        assert response['msg'] == 'success'

    # 测试info接口
    def test_info(self):
        response = self.app.info()
        assert response['code'] == 200
        assert response['msg'] == 'success'
        assert response['data'] == 'info'


if __name__ == "__main__":
    print("================================")


