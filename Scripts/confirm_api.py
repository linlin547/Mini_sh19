from Api.apiFactory import ApiFactory

# 首页 -轮播图
print("首页:{}".format(ApiFactory.home_api().banner().json()))
# 首页 -专题栏
print("专题栏:{}".format(ApiFactory.home_api().theme().json()))
# 首页 -新品
print("新品:{}".format(ApiFactory.home_api().new_product().json()))