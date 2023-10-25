age = int(input("Please enter your age: "))

if age < 18:
    print("You are younger than 18.")
elif age < 21:
    print("You are younger than 21")
elif age < 31:
    print("You are younger than 31.")
elif age > 31:
    print("You are older than 31.")


print("a" < "b")
print("b" < "a")
print("John" < "Terry")
print("john" < "Terry")


print(5 < 10.2)
print(str(5) < "Monty")
print("5" < "5")
#Task asks these to be input but gives error code due to data-types so fixed these to prevent the error from appearing.


new_age = 30
print(new_age >=18 and new_age <=65)
print(new_age <18 or new_age >65)
print(not new_age > 18)
print(age >= 18 and age <= 65) and (not age == 30)

weight = 150
height = 140
weight_between_100_and_200 = 100 < weight < 200
height_between_131_and_160 = 131 < height < 160


message = "Hello there, my name is John"
substring_true = "nam" in message
substring_false = "Pedro" in message


if age < 30 and age > 18:
    print("You are still young!")


if age > 100:
    print("you are very old,")
    print("well done!")
elif age > 80:
    print("you are fairly old")
    print("Pretty good!")
elif age > 40:
    print("you are middle-aged")
    print("never mind")
else:
    print("you are not very old - yet")

if age < 40 and age > 30:
    print("You are still not very old!")


name = input("Enter your name: ")
if bool(name):
    print("Your name is", name)
else:
    print("Name not entered")

print("you are an adult") if age >= 18 else print("you are not an adult, yet!")


names = ["Alice", "Bob", "Charlie", "David"]
for name in names:
    print(name)


for i in range(2, 11, 2):
    result = i ** i
    print(f"{i} to the power of {i} = {result}")


numbers = [10, 20, 30, 90, 200, 30, 22, 11]
total = 0
flag = False
for num in numbers:
    total += num
    print(f"Running total: {total}")
    if num > 100:
        print(f"Value {num} is greater than 100. Breaking out of the loop.")
        flag = True
        break
if not flag:
    print("All numbers processed")

