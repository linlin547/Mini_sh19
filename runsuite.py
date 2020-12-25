from Utils.HTMLTestRunner import HTMLTestRunner
import unittest
from Scripts.test_home import TestHome
from Scripts.test_product import TestProduct
from Scripts.test_user import TestUser
from Scripts.test_order import TestOrder

# 测试套件
suite = unittest.TestSuite()

suite_list = [TestHome, TestProduct, TestUser, TestOrder]
# suite_list = [TestUser]

for i in suite_list:
    # 添加测试类
    suite.addTest(unittest.makeSuite(i))

# 测试报告位置
report_path = "./report.html"

# 编写
with open(report_path, "wb") as f:
    runner = HTMLTestRunner(f, title="小程序", description="v1.1")
    # 执行
    runner.run(suite)
