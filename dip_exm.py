# Dependency Inversion principle
# high-level module should not depend upon low-level module
# both should be depend upon abstractions


class Manager(object):
    def __init__(self):
        self.developer = []
        self.tester = []
        self.designer = []

    def add_developer(self, dev):
        self.developer.append(dev)

    def add_tester(self, tester):
        self.tester.append(tester)

    def add_designer(self, desg):
        self.designer.append(desg)


class Developer(object):
    def __init__(self):
        print('developer added')


class Tester(object):
    def __init__(self):
        print('tester added')


class Designer(object):
    def __init__(self):
        print('designer added')


# abstraction should not be depend upon details, details should depend upon abstractions


class Employee(object):
    def work(self):
        pass


class Manager:
    def __init__(self):
        self.employee = []

    def add_employee(self, emp):
        self.employee.append(emp)


class Developer(Employee):
    def __init__(self):
        print('developer added')

        def work():
            print('Work done!!!')


class Tester(Employee):
    def __init__(self):
        print('tester added')

        def work():
            print('Work done!!!')


class Designer(Employee):
    def __init__(self):
        print('designer added')

        def work():
            print('Work done!!!')


class QA(Employee):
    def __init__(self):
        print('QA added')

        def work():
            print('Work done!!!')
