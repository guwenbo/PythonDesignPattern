#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from context import Context
from strategy import *

if __name__ == "__main__":
    con = Context(strategy=ConcreteStrategyA())
    con.exec_strategy()

    con = Context(strategy=ConcreteStrategyB())
    con.exec_strategy()
