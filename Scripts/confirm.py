from Api.homeApi import HomeApi
from Api.productApi import ProductApi
from Api.userApi import UserApi
from Utils import app
from Api.orderApi import OrderApi

# # 轮播图
# print("轮播图:{}".format(HomeApi().banner().json()))
#
# # 专题栏
# print("专题栏:{}".format(HomeApi().theme().json()))
#
# # 最近新品
# print("最近新品:{}".format(HomeApi().new_product().json()))


# 商品分类
# print("分类:{}".format(ProductApi().category().json()))
# # 分类下商品
# print("分类下商品:{}".format(ProductApi().product(4).json()))  # 校验分类4
# # 商品详情
# print("商品详情:{}".format(ProductApi().detail(17).json()))  # 商品id17

# # 创建token
# res = UserApi().create_token().json()
# print("创建token返回值:{}".format(res))
# # 保存token
# app.header["token"] = res.get("token")

# # 验证token
# print("验证token:{}".format(UserApi().verify_token().json()))
#
# # 获取地址
# print("地址信息:{}".format(UserApi().user_address().json()))
# 创建订单
# print("创建:{}".format(OrderApi().create_order(2, 1).json()))
#
# # 查询订单
# print("查看:{}".format(OrderApi().query_order(103).json()))

# 用户订单列表
print("列表:{}".format(OrderApi().user_order(1).json()))
