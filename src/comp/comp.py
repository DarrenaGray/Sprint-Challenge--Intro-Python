# The following list comprehension exercises will make use of the
# defined Human class.
import math


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"


humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [first.name for first in humans if first.name[0] == "D"]

# Second way:
# a = []
# for first in humans:
#     if first.name[0] == 'D':
#         a.append(first.name)

print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [last.name for last in humans if last.name[-1] == 'e']

# Second way:
# b = []
# for last in humans:
#     if last.name[-1] == 'e':
#         b.append(last.name)

print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")

start = ("C", "D", "E", "F", "G")

c = [between.name for between in humans if between.name.startswith(start)]

# c = []

# Second way:
# for between in humans:
#     if between.name.startswith(start):
#         c.append(between.name)
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [ages.age + 10 for ages in humans]

# Second way:
# d = []

# for ages in humans:
#     d.append(ages.age + 10)

print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [f"{hyphen.name}-{hyphen.age}" for hyphen in humans]

# Second way:
# e = []

# for hyphen in humans:
#     e.append(f"{hyphen.name}-{hyphen.age}")

print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(name_age.name, name_age.age)
     for name_age in humans if name_age.age in range(27, 33)]

# Second way:
# f = []
# for name_age in humans:
#     if name_age.age in range(27, 33):
#         f.append((name_age.name, name_age.age))

print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")

g = [Human(uppercase.name.upper(), uppercase.age + 5) for uppercase in humans]

# Second way:
# g = []

# for uppercase in humans:
#     g.append(Human(uppercase.name.upper(), uppercase.age + 5))

# print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")

h = [math.sqrt(sqr_root.age) for sqr_root in humans]

# Second way:
# h = []

# for sqr_root in humans:
#     h.append(math.sqrt(sqr_root.age))

print(h)
