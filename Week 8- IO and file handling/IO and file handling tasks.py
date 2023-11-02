width = 104.32
height = 15.654
area = width % height
print(f"The area of a rectangle with a width of {width} and a height of {height} is {area:.3f}.")


name = input("Please input your name: ")
age = int(input("Please enter your age: "))
print(f"{name:15} - {age:10}")
print(f"{name:10} - {age:20}")
print(f"{name:20} - {age:30}")
print(f"{name:*>20} - ${age:.2f:>20}")


r = 52
area = 3.14159 * r**2
print(f"The area of a circle with a radius of {r} is {area:.2f} square units.".format(r=r, area=area))
