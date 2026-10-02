class Car:
    def move(self):
        print("The car drives on the road.")


class Person:
    def move(self):
        print("The person walks on foot.")


class Robot:
    def move(self):
        print("The robot moves using its mechanical parts.")


def make_it_move(thing):
    thing.move()


car = Car()
person = Person()
robot = Robot()

things = [car, person, robot]

for thing in things:
    make_it_move(thing)