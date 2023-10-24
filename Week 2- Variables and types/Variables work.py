total = 100
print("The total is, ", total)

total = total + 99
print("The total is now,", total)

total -= 1
print("The total is", total)
total *= 4
print("The total is", total)
total /= 2
print("The total is", total)

total2 = 98.2
count = 5

average = total2 / count
print("The average of 98.2 and 5 is", average)

print(type(False))
print(type(1000))
print(type(100.111))
print(type("Hello"))
print(type(True))
print(type(100 / 5))
print(type(100 // 5))

print("ABC" * 10)


name = "Pedro B"
address = "Hogwarts"
contact_details = "Email: pedro@email.com \nPhone: +44 077832 2343"

print("Name:", name)

print("Address:", address)

print("Contact Details:")
print(contact_details)

name_length = len(name)
print("Length of Name:", name_length)

age = int(input("Enter your age: "))
print("in one year your age will be", age + 1)

value = int(input("Please enter a value:"))
value2 = int(input("Please enter a value:"))

result = value * value2
print("This is the result of those two values multiplied,", result)

comment = "I would have \"thought\" you knew better!"

text_to_display = "This text includes characters such as '\\', '\"' and \"'\",\n\tThis is a new line that starts with a tab\n\t\tThis new line starts with two tabs"
print(text_to_display)

text_to_display = "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\nHello there!\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"
print(text_to_display)

text_to_display = '''This text spans three lines,
and includes both single ('),
and double quotes (").'''
print(text_to_display)

surname = "Palin"
third_letter = surname[2]
print(third_letter)
last = surname[-2]
print(last)
middle = surname[1:]
print(middle)
characters_except_last = surname[:-1]
print(characters_except_last)

primes = [2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
first_four_primes = primes[:4]
print(first_four_primes)

names = ["John", "Sarah", "Michael", "Emily", "Daniel"]
names[-1:-1] = ["Tim", "Bill"]
print(names)

nums = [1, 2, 3] * 5
print(nums)
