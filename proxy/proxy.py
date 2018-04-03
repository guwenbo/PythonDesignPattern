from subject import *


class Proxy(Subject):

    def __init__(self, subject):
        if isinstance(subject, Subject):
            self._subject = subject
        else:
            raise TypeError("Invalid Subject Type...")

    def request(self):
        if self._subject:
            print("Request from proxy...")
            self._subject.request()
