# 组织登录和添加员工套件
# 导包
import unittest
# 组织测试套件
import time

import app
from case.testIHRMEmp import TestEmployee
from case.testLogin import TestUser
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(TestUser("test_success_login"))
suite.addTest(TestEmployee("test_emp_add"))
suite.addTest(TestEmployee("test_emp_update"))
suite.addTest(TestEmployee("test_emp_check"))
suite.addTest(TestEmployee("test_emp_delete"))
# 执行测试套件
report_path = app.RPO_PATH + "/report/report-{}.html".format(time.strftime("%Y%m%d%H%M%S"))
with open(report_path,"wb") as f:
    runner = HTMLTestRunner(f,title = "人力资源测试报告",description="v1.0")
    # runner= unittest.TextTestRunner()
    runner.run(suite)