class NewEmployee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = "pranali"
        self.last = "namdas"


emp1 = NewEmployee('john', 'sena')

emp1.fullname = 'jim shergill'

print(emp1.first)
print(emp1.email)
print(emp1.fullname)

del emp1.fullname

print(emp1.fullname)

# TODO: advantage of property over method, when should property
# TODO: list out all decorators
