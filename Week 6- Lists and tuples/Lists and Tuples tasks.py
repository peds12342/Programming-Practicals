import math

squares = [4, 9, 16, 25]

for num in squares:
    square_root = math.sqrt(num)
    print(f"The square root of {num} is {square_root}")


squares.append(49)
squares.append(64)
squares.append(81)

print(squares)


next_squares = [121, 144, 169]
squares.extend(next_squares)
print(squares)


squares.insert(0, 2)
print(squares)


squares.remove(49)
print(squares)


value_to_remove = 3
if value_to_remove in squares:
    squares.remove(value_to_remove)
    print(f"Removed {value_to_remove} from the list")
else:
    print(f"{value_to_remove} is not in the list")
print(squares)


list = [1, 2, 3, 1, 2]
list.remove(2)
print(list)


last_value = squares.pop()
print(f"Removed value: {last_value}")
print(squares)


first_value = squares.pop(0)
print(f"Removed value: {first_value}")
print(squares)


names = ["Eric", "anna", "Sophie", "sam"]
names.sort()
print(names)


names.sort(key=lambda x: x.upper())
print(names)


squares.reverse()
print(squares)


colours = ["red", "green", "yellow", "blue", "red"]
index_of_blue = colours.index("blue")
print(index_of_blue)


colours_copy = colours.copy()
colours[0] = "orange"
colours.append("purple")
print("Original List:", colours_copy)
print("New List:", colours)


cubes = [x ** 3 for x in range(2, 21)]
print(cubes)


all_users = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "George", "Hannah"]
some_users = [u for u in all_users if len(u) < 8]
print(f"These users met the requirements to be on the list: {some_users}")
#This code makes it so that any usernames in all_users that have less than 8 characters will enter the some_users list.


address = (8, "Ham", "12345")
house_number, street, postcode = address


the_one = ("Neo",)
print(the_one)

print("House Number:", house_number)
print("Street:", street)
print("Postcode:", postcode)


print(*address)
print(address)
