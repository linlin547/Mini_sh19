from Api.apiFactory import ApiFactory
import unittest
from Utils.auto_assert import auto
from Utils.analysis_data import AnalysisData
from parameterized import parameterized


# def home_data():
#     # banner值
#     banner_list = []
#     # theme值
#     theme_list = []
#     # new值
#     new_list = []
#     # 读json文件数据
#     json_data = AnalysisData.get_json_data("home.json")
#     # 解析-banner 组装成[()]
#     for i in json_data.get("banner"):
#         banner_list.append((i.get("banner_code"), i.get("banner_id"),
#                             i.get("banner_name"), i.get("banner_length")))
#     # 解析-theme 组装成[()]
#     for o in json_data.get("theme"):
#         theme_list.append((o.get("theme_code"), o.get("theme_ids"),
#                            o.get("theme_length_url"), o.get("theme_name")))
#     # 解析-new 组装成[()]
#     for x in json_data.get("new_product"):
#         new_list.append((x.get("new_code"), x.get("new_length"),
#                          x.get("new_keys")))
#
#     return {"banner": banner_list, "theme": theme_list, "new": new_list}


class TestHome(unittest.TestCase):
    # @parameterized.expand(home_data().get("banner"))
    @parameterized.expand(
        AnalysisData.get_json_data("home.json", "banner", ["banner_code", "banner_id", "banner_name", "banner_length"]))
    def test_banner(self, banner_code, banner_id, banner_name, banner_length):
        """

        :param banner_code: 状态码
        :param banner_id: id
        :param banner_name: name
        :param banner_length: items长度大于0
        :return:
        """
        print(
            "banner_code:{}, banner_id:{}, banner_name:{}, banner_length:{}".format(banner_code, banner_id, banner_name,
                                                                                    banner_length))
        # 请求
        res = ApiFactory.home_api().banner()
        # 断言 -状态码
        auto(self, res.status_code, banner_code)
        # 断言 id
        auto(self, res.json().get("id"), banner_id)
        # 断言 name
        auto(self, res.json().get("name"), banner_name)
        # 断言items长度大于0
        auto(self, len(res.json().get("items")), banner_length, tag="more")
        # 断言图片utl不为空
        auto(self, len(res.json().get("items")[0].get("img").get("url")), banner_length, tag="more")

    # @parameterized.expand(home_data().get("theme"))
    @parameterized.expand(
        AnalysisData.get_json_data("home.json", "theme", ["theme_code", "theme_ids", "theme_length_url", "theme_name"]))
    def test_theme(self, theme_code, theme_ids, theme_length_url, theme_name):
        """

        :param theme_code: 状态码
        :param theme_ids: id=1 id=2 id =3
        :param theme_length_url: 长度 -url
        :param theme_name: 专题名字
        :return:
        """
        print("theme_code:{}, theme_ids:{}, theme_length_url:{}, theme_name:{}".format(theme_code, theme_ids,
                                                                                       theme_length_url, theme_name))
        # 请求
        res = ApiFactory.home_api().theme()
        # 断言 -状态码
        auto(self, res.status_code, theme_code)
        # 断言 -id=1 id=2 id =3
        for i in theme_ids:
            auto(self, i, res.text, tag="in")
        # 断言 长度
        auto(self, len(res.json()), theme_length_url, tag="more")
        # 断言 -name
        auto(self, res.json()[0].get("name"), theme_name)
        # 断言 -url
        auto(self, len(res.json()[0].get("topic_img").get("url")), theme_length_url, tag="more")

    # @parameterized.expand(home_data().get("new"))
    @parameterized.expand(
        AnalysisData.get_json_data("home.json", "new_product", ["new_code", "new_length", "new_keys"]))
    def test_new_product(self, new_code, new_length, new_keys):
        """

        :param new_code: 状态码
        :param new_length: 长度
        :param new_keys: 关键字段
        :return:
        """
        print("new_code:{}, new_length:{}, new_keys:{}".format(new_code, new_length, new_keys))
        # 请求
        res = ApiFactory.home_api().new_product()
        # 断言 -状态码
        auto(self, res.status_code, new_code)
        # 断言 - 长度
        auto(self, len(res.json()), new_length, tag="more")
        # 断言 -关键字段
        for i in new_keys:
            auto(self, i, res.text, tag="in")
