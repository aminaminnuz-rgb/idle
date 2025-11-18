     
def search_item(items_list, target):
    count = 0
    for item in items_list:
        if item == target:
            count += 1
    return count


user_input = input("Enter a list of items separated by commas: ")
items = user_input.split(",")


search = input("Enter the item to search for: ")


result = search_item(items, search)
print(f"'{search}' occurred {result} times in the list.")    


    