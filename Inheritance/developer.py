from Inheritance.employee import Employee


class Developer(Employee):
    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, fname, lname, pay, employees=None):
        super().__init__(fname, lname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print(emp.emp_fullname())


dev1 = Developer('john', 'sena', 50000, 'python')
dev2 = Developer('harry', 'potter', 60000, 'java')

mng1 = Manager('sue', 'smith', 90000, [dev1])

print(mng1.emp_email())

mng1.add_emp(dev2)

mng1.print_emp()

print(isinstance(mng1, Manager))
print(isinstance(mng1, Employee))
print(isinstance(dev1, Developer))
print(isinstance(dev1, Manager))

print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))
