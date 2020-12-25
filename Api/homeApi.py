import requests
from Utils import app


class HomeApi:

    def __init__(self):
        # 轮播图
        self.banner_url = app.host_url + "/banner/{}"
        # 专题栏
        self.theme_url = app.host_url + "/theme"
        # 新品
        self.new_url = app.host_url + "/product/recent"

    def banner(self, banner_id=1):
        """
        轮播图
        :param banner_id: 轮播图id
        :return: 响应对象
        """
        return requests.get(self.banner_url.format(banner_id))

    def theme(self, ids="1,2,3"):
        """
        专题栏
        :param ids: 专题id值 单个 多个
        :return: 响应对象
        """
        # 数据
        data = {"ids": ids}
        return requests.get(self.theme_url, params=data)

    def new_product(self):
        """
        最近新品
        :return: 响应对象
        """
        return requests.get(self.new_url)
