import math

number = int(input("Please enter a number (e.g 2401) to find it's square root: "))
square_root = math.sqrt(number)
print(f"This is the square root of the number you entered {square_root}!")


from math import log2
result = log2(number)
print(f"The base-2 logarithm of {number} is {result}")


def displaytwice(msg):
    """ This function takes a message (msg) as input and prints it twice."""
    print(msg)
    print(msg)
displaytwice("Hello World.")
displaytwice("This is a test message!")


def findMax(a, b):
    """Finds the maximum of two values."""
    if a > b:
        max_value = a
    else:
        max_value = b
    return max_value


value1 = int(input("Please enter a number: "))
value2 = int(input("Please enter a number: "))
max = findMax(value1, value2)
print(f"The max of the two values is {max}!")


def multiply_values(a, b=None):
    if b is None:
        return a * a
    else:
        return a * b
result1 = multiply_values(5, 3)
result2 = multiply_values(4)
result3 = multiply_values(7, 7)
print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)


def someFunc(x, y, z):
    print(f'x is {x}')
    print(f'y is {y}')
    print(f'z is {z}')
someFunc(y=2, z=3, x=1)
someFunc(z=3, x=1, y=2)
someFunc(z=3, y=2, x=1)
someFunc(x=1, y=2, z=3)


print("Apple", "Banana", "Cherry", sep=', ')
print("One", "Two", "Three", sep=' - ')
print("Red", "Green", "Blue", sep='\n')


def calcAve(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)
average1 = calcAve(10, 20, 30)
print(average1)
average2 = calcAve(15, 25, 35, 45, 55)
print(average2)
average3 = calcAve(5, 12)
print(average3)


hypot = lambda a,b : math.sqrt(a * a + b * b)
hypot(3,4)
print(type(hypot))


to_seconds = lambda hours, minutes = 0: (hours * 3600) + (minutes * 60)
print(to_seconds(2, 30))
print(to_seconds(1, 15))
print(to_seconds(0, 45))

print(to_seconds(1))
print(to_seconds(2))
