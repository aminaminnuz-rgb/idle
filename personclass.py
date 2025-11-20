class Person:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

class Marks:
    def __init__(self,maths,cs):
        self.maths = maths
        self.cs = cs

class Student (Person, Marks):
    def __init__(self,name,roll,maths,cs):
        Person.__init__(self,name,roll)
        Marks.__init__(self,maths,cs)

    def display(self):
        total = self.maths + self.cs
        percentage = total / 2

        print("Student Details")
        print("Name:",self.name) 
        print("Roll No :",self.roll)
        print("Mrks Maths :",self.maths)
        print("Mrks cs :",self.cs)

        if percentage > 50 :
            print("Result: pass")
        else:
            print("Result: fail")

name = input("Enter Name:")
             




        