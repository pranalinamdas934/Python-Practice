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
