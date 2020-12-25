from Utils import app
import requests


class OrderApi:

    def __init__(self):
        # 创建订单
        self.create_order_url = app.host_url + "/order"
        # 查看订单
        self.query_order_url = app.host_url + "/order/{}"
        # 用户订单列表
        self.user_order_url = app.host_url + "/order/by_user"

    def create_order(self, product_id=8, count=1):
        """
        创建订单
        :param product_id: 商品id
        :param count: 购买数量
        :return:
        """
        # 数据
        data = {"products": [{"product_id": product_id, "count": count}]}

        # 请求
        return requests.post(self.create_order_url, headers=app.header, json=data)

    def query_order(self, order_id=50):
        """
        查询订单
        :param order_id: 订单id
        :return:
        """
        return requests.get(self.query_order_url.format(order_id), headers=app.header)

    def user_order(self, page=1):
        """
        用户订单
        :param page: 获取订单列表页数
        :return:
        """
        # 数据
        data = {"page": page}

        return requests.get(self.user_order_url, params=data, headers=app.header)
