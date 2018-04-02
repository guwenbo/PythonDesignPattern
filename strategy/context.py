from strategy import Strategy


class Context(object):
    def __init__(self, strategy):
        if isinstance(strategy, Strategy):
            self._strategy = strategy
        else:
            raise TypeError("not a strategy type")

    def exec_strategy(self):
        self._strategy.exec_strategy()
