from Utils import app
import requests


class ProductApi:

    def __init__(self):
        # 商品分类
        self.category_url = app.host_url + "/category/all"
        # 分类下商品
        self.product_url = app.host_url + "/product/by_category"
        # 商品详情
        self.detail_url = app.host_url + "/product/{}"

    def category(self):
        """
        商品分类
        :return: 响应对象
        """
        return requests.get(self.category_url)

    def product(self, category_id=2):
        """
        分类下商品
        :param category_id: 分类id
        :return:
        """
        # 数据
        data = {"id": category_id}

        return requests.get(self.product_url, params=data)

    def detail(self, product_id):
        """
        商品详情
        :param product_id: 商品id
        :return:
        """
        return requests.get(self.detail_url.format(product_id))
