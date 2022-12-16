class Vehicle:

    def __init__(self, position: ()):  # position: кортеж (10, 20)
        self.position = position

    def travel(self, destination):
        route = self.calculate_route(source=self.position, to=destination)
        self.move_along(route)

    @staticmethod
    def calculate_route(source, to):
        return 0  # to be realized

    def move_along(self, route):
        print("moving")

class Mixin:

    # def __init__(self, id):
    #     self.it = id

    def turn_on_radio(self, it):
        print(f'Playing {it}')

class Car(Vehicle, Mixin):
    def __init__(self, position2):
        self.position2 = position2
        # self.position2 = position2
        super().__init__(position2)

class Airplane(Vehicle):
    pass
car = Car((10, 20))
car.turn_on_radio('Moscow FM')


# Playing Moscow FM
