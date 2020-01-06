class Shape(object):
    shape = ""

    def draw(self):
        return self.shape


class Circle(Shape):
    shape = "circle"


class Triangle(Shape):
    shape = "triangle"


class Square(Shape):
    shape = "square"


class ShapeFactory:
    def create_shape(self, typ):
        cls_typ = typ.capitalize()
        return globals()[cls_typ]()


shape_obj = ShapeFactory()
shapes = ['circle', 'triangle', 'square']
for shape in shapes:
    print(shape_obj.create_shape(shape).draw())


# NOTE: passing in shapes to ShapeFactory becomes abstract factory pattern
# one practical example from python language

class Obstacle:
    def action(self): pass


class Character:
    def interactWith(self, obstacle): pass


class Kitty(Character):
    def interactWith(self, obstacle):
        print("Kitty has encountered a",
              obstacle.action())


class KungFuGuy(Character):
    def interactWith(self, obstacle):
        print("KungFuGuy now battles a",
              obstacle.action())


class Puzzle(Obstacle):
    def action(self):
        print("Puzzle")


class NastyWeapon(Obstacle):
    def action(self):
        print("NastyWeapon")


# The Abstract Factory:
class GameElementFactory:
    def makeCharacter(self): pass

    def makeObstacle(self): pass


# Concrete factories:
class KittiesAndPuzzles(GameElementFactory):
    def makeCharacter(self): return Kitty()

    def makeObstacle(self): return Puzzle()


class KillAndDismember(GameElementFactory):
    def makeCharacter(self): return KungFuGuy()

    def makeObstacle(self): return NastyWeapon()


class GameEnvironment:
    def __init__(self, factory):
        self.factory = factory
        self.p = factory.makeCharacter()
        self.ob = factory.makeObstacle()

    def play(self):
        self.p.interactWith(self.ob)


g1 = GameEnvironment(KittiesAndPuzzles())
g2 = GameEnvironment(KillAndDismember())
g1.play()
g2.play()
