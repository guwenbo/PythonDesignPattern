#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from factory import *

if __name__ == '__main__':
    fact = FactoryA()
    prod = fact.create_product()
    prod.operate()
