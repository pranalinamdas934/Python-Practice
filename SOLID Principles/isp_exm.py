# Interface segregation principle


class IShape:
    def draw_circle(self):
        raise NotImplementedError

    def draw_triangle(self):
        raise NotImplementedError

    def draw_square(self):
        raise NotImplementedError


class Circle(IShape):
    def draw_circle(self):
        pass

    def draw_triangle(self):
        pass

    def draw_square(self):
        pass


class Triangle(IShape):

    def draw_circle(self):
        pass

    def draw_triangle(self):
        pass

    def draw_square(self):
        pass


class Square(IShape):

    def draw_circle(self):
        pass

    def draw_triangle(self):
        pass

    def draw_square(self):
        pass


# Interface segregation principle
# client should not be forced to depend upon that they do not use

class IShape:
    def draw(self):
        raise NotImplementedError


class Circle(IShape):
    def draw(self):
        pass


class Triangle(IShape):
    def draw(self):
        pass


class Square(IShape):
    def draw(self):
        pass
