class dog:
    height = 200
    satiety = 100
    age = 1000

class cat(dog):
    satiety = 10

class turtle(dog):
    age = 100

    def __init__(self):
        print(self.age)
        print(self.height)
        print(self.satiety)
nick = turtle()