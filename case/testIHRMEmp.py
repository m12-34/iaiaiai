"""员工增删改查测试用例"""
#导包
import unittest
import requests

# 定义测试类
from API.EmpAPI import UserEmp


class TestEmployee(unittest.TestCase):
    # 初始化方法
    def setUp(self):
        self.session = requests.Session()
        self.user_emp = UserEmp()
    # 资源销毁路径
    def tearDown(self):
        self.session.close()
    # 测试用例1.增
    def test_emp_add(self):
        response_add = self.user_emp.get_emp_add(self.session,"balalalaxiasdxian","18878876667")
        print(response_add.json())
        id = response_add.json().get("data").get("id")
        print(id)
    # 测试用例2.改
    def test_emp_update(self):
        response = self.user_emp.get_emp_update(self.session,"1184386691976482816","balaladamoxian")
        print(response.json())
        self.assertEqual(True,response.json().get("success"))


    # 测试用例3.查
    def test_emp_check(self):
        response = self.user_emp.get_emp_check(self.session,"1184386691976482816")
        print(response.json())
        self.assertEqual(True,response.json().get("success"))

    # 测试用例4.删
    def test_emp_delete(self):
        response = self.user_emp.get_emp_delete(self.session,"1184386691976482816")
        print(response.json())
        self.assertEqual(True,response.json().get("success"))