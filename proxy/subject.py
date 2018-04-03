class Subject(object):

    def request(self):
        pass


class RealSubject(Subject):

    def request(self):
        print("True request...")
