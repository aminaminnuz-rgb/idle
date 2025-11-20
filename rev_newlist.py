def reverse_items(lst):
    return [str(item)[::-1] for item in lst]

items = ["apple", "banana", "cat"]
result = reverse_items(items)
print(result)  
