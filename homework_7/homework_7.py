class Auto:
    def __init__(self,brand,age,mark,color="red",weight=1500):

        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age+=1
        print(self.age)


truck = Auto("Audi","2","xc90",weight= 1800)


truck.move()
truck.stop()
truck.birthday()

