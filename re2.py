import re
pattern = re.compile(r"\bs\w*e\b",re.IGNORECASE)

with open("input.txt", "r") as file:
    for line in file:
        if pattern.search(line):
            print(line.strip())
