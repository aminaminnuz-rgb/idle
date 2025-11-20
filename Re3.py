def join_recursive(lst, index=0):
    # Base case: if only one element left, return it as string
    if index == len(lst) - 1:
        return str(lst[index])
    
    # Recursive step: current element + '-' + result of next elements
    return str(lst[index]) + '-' + join_recursive(lst, index + 1)


# Example
items = ["apple", "banana", "cherry", "dates"]
result = join_recursive(items)
print(result)
