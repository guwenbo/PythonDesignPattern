#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from component import *
from decorator import *

if __name__ == '__main__':
    con = ConcreteComponent()

    performance_decorator = PerformanceDecorator()
    performance_decorator.set_component(con)

    logger_decorator = LogDecorator()
    logger_decorator.set_component(performance_decorator)

    logger_decorator.operate()
