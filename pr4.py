def even_odd(numbers):
    for item in numbers:
        if item == 237:
            break
        if item % 2 == 0:
            print(item)

# Get input from the user
n = input("Enter integers separated by spaces: ")
n = list(map(int, n.split()))  # Convert input string to list of integers

even_odd(n)
