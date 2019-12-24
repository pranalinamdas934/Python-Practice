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
