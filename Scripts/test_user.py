import unittest
from Api.apiFactory import ApiFactory
from Utils import app
from Utils.auto_assert import auto
from Utils.analysis_data import AnalysisData
from parameterized import parameterized


class TestUser(unittest.TestCase):
    @parameterized.expand(AnalysisData.get_json_data("user.json", "token", ["token_code", "token_length"]))
    def test_1token(self, token_code, token_length):
        """
        获取token
        :param token_code: 状态码
        :param token_length: token长度
        :return:
        """

        # 请求
        res = ApiFactory.user_api().create_token()
        # 断言 -状态码
        auto(self, res.status_code, token_code)
        # 断言 -token不为空
        auto(self, len(res.json()), token_length, "more")
        # 存储token到app.header
        app.header["token"] = res.json().get("token")
        print("app:{}".format(app.header))

    @parameterized.expand(AnalysisData.get_json_data("user.json", "verify", ["verify_code", "verify_isValid"]))
    def test_verify(self, verify_code, verify_isValid):
        """
        验证token
        :param verify_code: 状态码
        :param verify_isValid: isValid为True
        :return:
        """
        # 请求
        res = ApiFactory.user_api().verify_token()
        # 断言 -状态码
        auto(self, res.status_code, verify_code)
        # 断言 -isValid为True
        auto(self, res.json().get("isValid"), verify_isValid)

    @parameterized.expand(
        AnalysisData.get_json_data("user.json", "address", ["address_code", "address_name", "address_mobile"]))
    def test_address(self, address_code, address_name, address_mobile):
        """
        地址
        :param address_code: 状态码
        :param address_name: 姓名
        :param address_mobile: 手机号
        :return:
        """
        # 请求
        res = ApiFactory.user_api().user_address()
        # 断言-状态码
        auto(self, res.status_code, address_code)
        # 断言-姓名
        auto(self, res.json().get("name"), address_name)
        # 断言-手机号
        auto(self, res.json().get("mobile"), address_mobile)
