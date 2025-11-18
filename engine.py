class Engine:
    def __init__(self, power):
        self.__power = power

    def display(self):
        print("Engine power:", self.__power)

class Wheels:
    def __init__(self, size):
        self.__size = size

    def display(self):
        print("Wheel size:", self.__size)

class Car(Engine,Wheels):
    def __init__(self, model,power,size):
        Engine.__int__(self,power)
        Wheels.__int__(self,size)
        self.__model= model


    def display(self):
        print("Car Model:", self.__model)
        super().display()
        Wheels.display(self)

c1 = Car("Fortuner","2000","18 inch")
c1.display()        


