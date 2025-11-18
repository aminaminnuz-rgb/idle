import math

class Complex:
    # Constructor
    def __init__(self, real=0, imag=0):
        self.__real = real        # private attribute
        self.__imag = imag        # private attribute

    # Method to compute magnitude
    def magnitude(self):
        return math.sqrt(self.__real**2 + self.__imag**2)

    # Overload >= operator
    def __ge__(self, other):
        return self.magnitude() >= other.magnitude()

    # Optional: display
    def __str__(self):
        return f"{self.__real} + {self.__imag}i"


# Example usage:
c1 = Complex(3, 4)   # magnitude = 5
c2 = Complex(1, 2)   # magnitude ≈ 2.23

print("c1 =", c1)
print("c2 =", c2)

if c1 >= c2:
    print("c1 is greater than or equal to c2")
else:
    print("c1 is smaller than c2")
