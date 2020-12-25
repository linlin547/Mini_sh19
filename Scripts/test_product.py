import unittest
from Api.apiFactory import ApiFactory
from Utils.auto_assert import auto
from Utils.analysis_data import AnalysisData
from parameterized import parameterized


class TestProduct(unittest.TestCase):
    @parameterized.expand(AnalysisData.get_json_data("product.json", "category",
                                                     ["category_code", "category_length", "category_name"]))
    def test_category(self, category_code, category_length, category_name):
        """
        商品分类
        :param category_code: 状态码
        :param category_length: 长度
        :param category_name: 分类名字
        :return:
        """
        print("category_code:{}, category_length:{}, category_name:{}".format(category_code, category_length, category_name))
        # 请求
        res = ApiFactory.product_api().category()
        # 断言 -状态码
        auto(self, res.status_code, category_code)
        # 断言 -长度大于0
        auto(self, len(res.json()), category_length, "more")
        # 断言 - 分类名字：炒货
        auto(self, category_name, res.text, "in")

    @parameterized.expand(AnalysisData.get_json_data("product.json", "product",
                                                     ["product_code", "category_id", "product_length", "product_name"]))
    def test_product(self, product_code, category_id, product_length, product_name):
        """
        分类下商品
        :param product_code: 状态码
        :param category_id: 分类id
        :param product_length: 长度
        :param product_name: 商品名字
        :return:
        """
        print("product_code:{}, category_id:{}, product_length:{}, product_name:{}".format(product_code, category_id, product_length, product_name))
        # 请求
        res = ApiFactory.product_api().product(category_id)
        # 断言 -状态码
        auto(self, res.status_code, product_code)
        # 断言 -长度
        auto(self, len(res.json()), product_length, "more")
        # 断言 -商品名字
        auto(self, product_name, res.text, "in")

    @parameterized.expand(AnalysisData.get_json_data("product.json", "detail",
                                                     ["product_id", "detail_code", "detail_name",
                                                      "detail_price", "detail_img_length"]))
    def test_detail(self, product_id, detail_code, detail_name, detail_price, detail_img_length):
        """
        商品详情
        :param product_id: 商品id
        :param detail_code: 状态码
        :param detail_name: 商品名字
        :param detail_price: 商品价格
        :param detail_img_length: 长度
        :return:
        """
        print("product_id:{}, detail_code:{}, detail_name:{}, detail_price:{}, detail_img_length:{}".format(product_id, detail_code, detail_name, detail_price, detail_img_length))
        # 请求
        res = ApiFactory.product_api().detail(product_id)
        # 断言 -状态码
        auto(self, res.status_code, detail_code)
        # 断言 -id
        auto(self, res.json().get("id"), product_id)
        # 断言 -name
        auto(self, res.json().get("name"), detail_name)
        # 断言 -price
        auto(self, res.json().get("price"), detail_price)
        # 断言 -main_img_url
        auto(self, len(res.json().get("main_img_url")), detail_img_length, "more")
