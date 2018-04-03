from product import *


class Factory(object):

    def create_product(self):
        pass


class FactoryA(Factory):

    def create_product(self):
        return ProductA()
