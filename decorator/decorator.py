from component import Component


class Decorator(Component):

    def __init__(self):
        self._component = None

    def set_component(self, component):
        self._component = component

    def operate(self):
        self._component.operate()


class LogDecorator(Decorator):

    def operate(self):
        print("Before log...")
        super().operate()
        print("After  log...")


class PerformanceDecorator(Decorator):
    def operate(self):
        print("Before performance monitor....")
        super().operate()
        print("After  performance monitor....")
