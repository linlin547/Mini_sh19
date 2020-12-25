from Api.homeApi import HomeApi
from Api.orderApi import OrderApi
from Api.productApi import ProductApi
from Api.userApi import UserApi


class ApiFactory:
    """
        前提：将来所有定义的接口类都需要在这里实例化
        返回所有接口类实例化对象
    """

    @classmethod
    def home_api(cls):
        """返回首页接口类对象"""
        return HomeApi()

    @classmethod
    def order_api(cls):
        """返回订单接口类对象"""
        return OrderApi()

    @classmethod
    def product_api(cls):
        """返回商品接口类对象"""
        return ProductApi()

    @classmethod
    def user_api(cls):
        """返回用户接口类对象"""
        return UserApi()
