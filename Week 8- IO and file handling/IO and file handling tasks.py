width = 104.32
height = 15.654
area = width % height
print(f"The area of a rectangle with a width of {width} and a height of {height} is {area:.3f}.")


name = input("Please input your name: ")
age = int(input("Please enter your age: "))
print(f"{name:15} - {age:10}")
print(f"{name:10} - {age:20}")
print(f"{name:20} - {age:30}")
print(f"{name:*>20} - ${age:.2f}")


r = 52
area = 3.14159 * r**2
print(f"The area of a circle with a radius of {r} is {area:.2f} square units.".format(r=r, area=area))


f_string = "{name:@^15} - {age:#^10}".format(name=name, age=age)
print(f_string)


f = open("info.txt")
file_contents = f.read()
f.close()


with open("info.txt", "r") as file:
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()


with open("info.txt", "r") as file:
    for line in file:
        print(line, end="")


with open("info.txt", "a") as file:
    file.write("This is an extra line\n")


with open("info.txt", "r") as file:
    for line in file:
        print(line, end="")
