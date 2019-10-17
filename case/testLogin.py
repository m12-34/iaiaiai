"""登录测试用例"""
# 导包
import json
import unittest
import requests
from parameterized import parameterized
import app
from API.UserAPI import UserLogin


# 定义类(继承 TestCase)
def read_json():
    data = []
    with open(app.RPO_PATH + "/data/login_data.json", "r", encoding="utf-8") as f:
        for value in json.load(f).values():
            mobile = value.get("moblie")
            password = value.get("password")
            success = value.get("success")
            code = value.get("code")
            message = value.get("message")
            data1 = (mobile, password, success, code, message)
            data.append(data1)
    return data


class TestUser(unittest.TestCase):
    # 初始化方法
    def setUp(self):
        # 初始化session
        self.session = requests.Session()
        # 初始化api 对象
        self.user_login = UserLogin()

    # 销毁资源路径
    def tearDown(self):
        self.session.close()

    # 测试用例、登录
    # 使用参数化
    @parameterized.expand(read_json())
    def test_login(self, mobile, password, success, code, message):
        # 调用请求业务
        response_login = self.user_login.login(self.session, mobile, password)

        # 调用断言业务
        self.assertEqual(success, response_login.json().get("success"))
        self.assertEqual(code, response_login.json().get("code"))
        self.assertIn(message, response_login.json().get("message"))

    # 登录成功的
    def test_success_login(self):
        print("*" * 100)
        response = self.user_login.login(self.session, "13800000002", "123456")
        print(response.json())
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

        token = response.json().get("data")
        app.TOKEN = token
