import json, os


class AnalysisData:
    @classmethod
    def get_json_data(cls, file, fk="", sk=[]):
        """
        读取json数据
        :param file: 文件名字 必须在./Data目录下
        :param fk: 数据文件父层级key名字
        :param sk: 父层级下子key的名字
        :return:
        """
        # 返回列表数据
        fk_list = []
        # os.sep 获取系统分隔符
        with open("./Data" + os.sep + file, "r", encoding="utf-8") as f:
            # with open(r"E:\Worker\Mini_sh19\Data" + os.sep + file, "r", encoding="utf-8") as f:
            # 读取json完整数据
            json_data = json.load(f)
            # 判断fk有值
            if fk:
                # 取fk对应的值 返回值是列表[{},{},{}]
                """
                [{
                    "desc": "轮播图",
                    "banner_code": 200,
                    "banner_id": 1,
                    "banner_name": "首页置顶",
                    "banner_length": 0
                  }]
                """
                value = json_data.get(fk)
                # 判断fk下sk的列表要有值 sk=["banner_code","banner_code"....]
                if sk:
                    # 遍历value列表
                    for i in value:
                        # 定义空列表 存储单个数据
                        sk_value = []
                        """
                        {
                            "desc": "轮播图",
                            "banner_code": 200,
                            "banner_id": 1,
                            "banner_name": "首页置顶",
                            "banner_length": 0
                          }
                        """
                        for x in sk:
                            # 数据列表 转为 元组
                            sk_value.append(i.get(x))
                        # 追加每一组数据到fk列表中
                        fk_list.append(tuple(sk_value))
                    return fk_list

#
# if __name__ == '__main__':
#     x = AnalysisData.get_json_data("home.json", "banner", ["banner_code", "banner_id", "banner_name", "banner_length"])
#     print(x)
