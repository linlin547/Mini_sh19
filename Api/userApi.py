from Utils import app

import requests


class UserApi:

    def __init__(self):
        # 创建token
        self.token_url = app.host_url + "/token/user"
        # 验证token
        self.verify_url = app.host_url + "/token/verify"
        # 获取地址
        self.address_url = app.host_url + "/address"

    def create_token(self):
        """
        创建token
        :return: 响应对象
        """
        # 数据
        data = {"code": app.code}
        return requests.post(self.token_url, headers=app.header, json=data)

    def verify_token(self):
        """
        验证token
        :return:
        """
        # 数据
        data = {"token": app.header.get("token")}  # 创建token测试脚本中添加到app文件里
        return requests.post(self.verify_url, headers=app.header, json=data)

    def user_address(self):
        """
        获取用地址
        :return:
        """
        return requests.get(self.address_url, headers=app.header)
