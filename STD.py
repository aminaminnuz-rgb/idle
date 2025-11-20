class Person:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll


class Marks:
    def __init__(self, maths, computer):
        self.maths = maths
        self.computer = computer


class Student(Person, Marks):
    def __init__(self, name, roll, maths, computer):
        Person.__init__(self, name, roll)
        Marks.__init__(self, maths, computer)

    def display(self):
        total = self.maths + self.computer
        percentage = total / 2

        print("---- Student Details ----")
        print("Name:", self.name)
        print("Roll No:", self.roll)
        print("Maths Marks:", self.maths)
        print("Computer Marks:", self.computer)
        print("Percentage:", percentage, "%")

        if percentage >= 50:
            print("Result: PASS")
        else:
            print("Result: FAIL")


# Main Program
name = input("Enter student name: ")
roll = input("Enter roll number: ")
maths = float(input("Enter Maths marks: "))
computer = float(input("Enter Computer marks: "))

s = Student(name, roll, maths, computer)
s.display()
