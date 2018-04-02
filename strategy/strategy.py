class Strategy(object):
    def exec_strategy(self):
        pass


class ConcreteStrategyA(Strategy):
    def exec_strategy(self):
        print("implement concrete strategy A")


class ConcreteStrategyB(Strategy):
    def exec_strategy(self):
        print("implement concrete strategy B")
