from copy import copy
from prototype import Prototype


class WorkExperience(Prototype):
    def __init__(self):
        self._work_date = None
        self._company = None

    def set_info(self, work_date, company):
        self._work_date = work_date
        self._company = company

    def clone(self):
        return copy(self)


class Resume(Prototype):
    def __init__(self, name='gin', age=23, sex='male', experience=WorkExperience()):
        self._name = name
        self._age = age
        self._sex = sex
        self._experience = experience

    def set_experience_info(self, work_date, company):
        self._experience.set_info(work_date, company)

    def clone(self):
        obj = copy(self)
        obj._experience = self._experience.clone()
        return obj

    def display(self):
        print(self._name, self._age, self._sex)
        print(self._experience._work_date, self._experience._company)
