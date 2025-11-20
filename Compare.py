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

    def percentage(self):
        return (self.maths + self.computer) / 2

    def result(self):
        return "PASS" if self.percentage() >= 50 else "FAIL"

    def display(self):
        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("Roll No:", self.roll)
        print("Maths:", self.maths)
        print("Computer:", self.computer)
        print("Percentage:", self.percentage())
        print("Result:", self.result())


# ----------- Main Program --------------
print("Enter details for Student 1")
s1 = Student(
    input("Name: "),
    input("Roll: "),
    float(input("Maths Marks: ")),
    float(input("Computer Marks: "))
)

print("\nEnter details for Student 2")
s2 = Student(
    input("Name: "),
    input("Roll: "),
    float(input("Maths Marks: ")),
    float(input("Computer Marks: "))
)

# Display details
s1.display()
s2.display()

# Compare the percentages
print("\n--- Comparison ---")
if s1.percentage() > s2.percentage():
    print(f"{s1.name} has a higher percentage.")
elif s2.percentage() > s1.percentage():
    print(f"{s2.name} has a higher percentage.")
else:
    print("Both students have equal percentage.")
