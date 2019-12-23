class Employee:
    raised_amt = 1.05

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def emp_email(self):
        return '{}.{}@gmail.com'.format(self.fname, self.lname)

    def emp_fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def emp_pay(self):
        self.pay = int(self.pay * self.raised_amt)
