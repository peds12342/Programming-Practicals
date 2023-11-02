names = {"John", "Eric", "Terry", "Michael", "Graham", "Terry"}
print(names)

sentence = "this is a sentence containing some letters"
unique_letters = {x for x in sentence}
print(sentence)


name = input("Enter your name: ")
if name not in names:
    print("You are not listed in the set of known names.")
else:
    print("You are listed in the set of known names.")


#print(help(set))


staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
directors = {"Kelly", "Rupert", "Cyril", "Jon"}
staff = staff.union({"Pedro", "Dan", "Alfie", "Thomas"})
print(staff)
staff_directors = staff.intersection(directors)
print(staff_directors)
external = directors.difference(staff)
print(external)
difference = staff.symmetric_difference(directors)
print(difference)


vowels = set({"a", "e", "i"})
vowels.update({"o", "u"})
print(vowels)

managers = {"Kelly", "Jon", "Paul", "Sally", "Sue"}
if managers.issubset(staff):
    print("All managers are staff members")
if staff.issuperset(managers):
    print("All managers are staff members")


#print(help(frozenset))


stock = {}
stock["pear"] = 50
if "apple" in stock:
    stock["apple"] += 1
else:
    stock["apple"] = 1
stock["kiwi"] = 10

#help(dict)

removed_pair = stock.popitem()
print("Removed:", removed_pair)
print("Updated stock:", stock)


import math
roots = {n: math.sqrt(n) for n in range(1, 26)}
for num, sqrt in roots.items():
    print(f"The square root of {num} is {sqrt}")
