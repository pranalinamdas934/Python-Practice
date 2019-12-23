# Single responsibility principle
# class should have only one responsibility

# access animal property


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        pass

# access to animal db


class AnimalDB:
    def get_animal(self, _id) -> Animal:
        pass

    def save(self, animal: Animal):
        pass
