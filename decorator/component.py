class Component(object):
    def operate(self):
        pass


class ConcreteComponent(Component):
    def operate(self):
        print("This is a concrete component")
