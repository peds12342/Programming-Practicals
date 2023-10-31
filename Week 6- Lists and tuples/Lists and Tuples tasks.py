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
