class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth


class Cuboid(Rectangle):
    def __init__(self, length, breadth, height):
        super().__init__(length, breadth)
        self.height = height

    def volume(self):
        return self.length * self.breadth * self.height

    # Overloading <= operator
    def __le__(self, other):
        return self.volume() <= other.volume()

    # For printing
    def __str__(self):
        return f"Cuboid({self.length}, {self.breadth}, {self.height}) Volume = {self.volume()}"


# ----------- Main Program -----------

print("Enter details for Cuboid 1")
c1 = Cuboid(
    float(input("Length: ")),
    float(input("Breadth: ")),
    float(input("Height: "))
)

print("\nEnter details for Cuboid 2")
c2 = Cuboid(
    float(input("Length: ")),
    float(input("Breadth: ")),
    float(input("Height: "))
)

# Display volumes
print("\n", c1)
print("", c2)

# Compare using overloaded <= operator
print("\n--- Comparison Based on Volume ---")

if c1 <= c2:
    print("Cuboid 1 has volume LESS THAN OR EQUAL to Cuboid 2.")
else:
    print("Cuboid 1 has GREATER volume than Cuboid 2.")
