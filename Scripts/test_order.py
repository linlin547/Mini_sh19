import unittest
from Api.apiFactory import ApiFactory
from Utils.auto_assert import auto
from Utils.analysis_data import AnalysisData
from parameterized import parameterized


class TestOrder(unittest.TestCase):
    @parameterized.expand(AnalysisData.get_json_data("order.json", "create_order",
                                                     ["product_id", "count", "create_code", "create_length",
                                                      "create_pass"]))
    def test_create_order(self, product_id, count, create_code, create_length, create_pass):
        """
        创建订单
        :param product_id: 商品id
        :param count: 购买数量
        :param create_code: 状态码
        :param create_length: order_id order_no 不为空
        :param create_pass: pass为True
        :return:
        """
        # 请求
        res = ApiFactory.order_api().create_order(product_id, count)
        # 断言 -状态码
        auto(self, res.status_code, create_code)
        # 断言 -order_id order_no 不为空
        auto(self, len(res.json().get("order_id")), create_length, "more")
        auto(self, len(res.json().get("order_no")), create_length, "more")
        # 断言 -pass为True
        auto(self, res.json().get("pass"), create_pass)

    @parameterized.expand(AnalysisData.get_json_data("order.json", "query_order",
                                                     ["order_id", "order_code", "order_no",
                                                      "order_price"]))
    def test_query_order(self, order_id, order_code, order_no, order_price):
        """
        查询订单
        :param order_id: 订单id
        :param order_code: 状态码
        :param order_no: 订单no
        :param order_price: 订单price
        :return:
        """
        # 请求
        res = ApiFactory.order_api().query_order(order_id)
        # 断言 -订单id
        auto(self, res.json().get("id"), order_id)
        # 断言 -订单no
        auto(self, res.json().get("order_no"), order_no)
        # 断言 -订单price
        auto(self, res.json().get("total_price"), order_price)
        # 断言 -状态码
        auto(self, res.status_code, order_code)

    @parameterized.expand(AnalysisData.get_json_data("order.json", "user_order",
                                                     ["user_code", "user_page", "user_list",
                                                      "user_keys"]))
    def test_user_order(self, user_code, user_page, user_list, user_keys):
        """
        查询用户订单列表
        :param user_code: 状态码
        :param user_page: 当前页数
        :param user_list: 订单列表长度
        :param user_keys: 关键字段
        :return:
        """
        # 请求
        res = ApiFactory.order_api().user_order(user_page)
        # 断言- 状态码
        auto(self, res.status_code, user_code)
        # 断言- 当前页数
        auto(self, res.json().get("current_page"), user_page)
        # 断言- 订单列表长度
        auto(self, len(res.json().get("data")), user_list, "more")
        # 断言- 关键字段
        for i in user_keys:
            auto(self, i, res.text, "in")
