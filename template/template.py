class AbstractClass(object):
    def template_method(self):
        print("This is template method...")
        self.sub_method()

    def sub_method(self):
        pass
