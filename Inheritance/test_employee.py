import unittest
from Inheritance.employee import Employee


class TestEmployee(unittest.TestCase):

    # runs at start of execution
    @classmethod
    def setUpClass(cls):
        print('setup class')

    # runs after all methods executes and finished
    @classmethod
    def tearDownClass(cls):
        print('teardown class')

    # create object before each method executes
    def setUp(self):
        print('setup')
        self.emp1 = Employee('john', 'sena', 5000)
        self.emp2 = Employee('harry', 'potter', 6000)

    # delete the created object after method executes
    def tearDown(self):
        print('teardown')

    def test_emp_email(self):
        print('email test')
        self.assertEqual(self.emp1.emp_email(), 'john.sena@gmail.com')
        self.assertEqual(self.emp2.emp_email(), 'harry.potter@gmail.com')

        self.emp1.fname = 'peter'
        self.emp2.fname = 'spancer'

        self.assertEqual(self.emp1.emp_email(), 'peter.sena@gmail.com')
        self.assertEqual(self.emp2.emp_email(), 'spancer.potter@gmail.com')

    def test_emp_fullname(self):
        print('fullname test')
        self.assertEqual(self.emp1.emp_fullname(), 'john sena')
        self.assertEqual(self.emp2.emp_fullname(), 'harry potter')

        self.emp1.fname = 'peter'
        self.emp2.lname = 'vency'

        self.assertEqual(self.emp1.emp_fullname(), 'peter sena')
        self.assertEqual(self.emp2.emp_fullname(), 'harry vency')

    def test_emp_pay(self):
        print('pay raised test')
        self.emp1.emp_pay()

        self.assertEqual(self.emp1.pay, 5250)
