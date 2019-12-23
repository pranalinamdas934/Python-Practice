# open/closed principle
# open for extension and closed for modification


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def make_noise(self):
        pass

    # animals = [
    #     Animal('lion'),
    #     Animal('mouse'),
    #     Animal('snake')
    # ]
    #
    # def animal_sound(animals: list):
    #     for animal in animals:
    #         if animal.name == 'lion':
    #             print('roar')
    #         elif animal.name == 'mouse':
    #             print('squeak')
    #         elif animal.name == 'snake':
    #             print('hiss')
    #
    # animal_sound(animals)


class Lion(Animal):
    def make_noise(self):
        return 'roar'


class Dog(Animal):
    def make_noise(self):
        return 'bark'


class Snake(Animal):
    def make_noise(self):
        return 'hiss'


class Mouse(Animal):
    def make_noise(self):
        return 'squeak'


# another example


# class Discount:
#     def __init__(self, customer, price):
#         self.customer = customer
#         self.price = price
#
#     def give_discount(self):
#         if self.customer == 'fav':
#             return self.price * 0.2
#         if self.customer == 'vip':
#             return self.price * 0.4
#

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        return self.price * 0.2


class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2


class SuperVIPDiscount(VIPDiscount):
    def get_discount(self):
        return super().get_discount() * 2
