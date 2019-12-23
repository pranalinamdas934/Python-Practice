# liskov substitution principle
# a sub-class should be substitutable for its super-class


# def animal_leg_count(animals: list):
#     for animal in animals:
#         if isinstance(animal, Lion):
#             print(lion_leg_count(animal))
#         elif isinstance(animal, Mouse):
#             print(mouse_leg_count(animal))
#         elif isinstance(animal, Pigeon):
#             print(pigeon_leg_count(animal))
#
# animal_leg_count(animals)

class Animal:
    def leg_count(self):
        pass


class Lion(Animal):
    def leg_count(self):
        pass
