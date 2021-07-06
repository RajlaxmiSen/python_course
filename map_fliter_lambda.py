names = ["tom", "richard", "harold"]
names = [name.title() for name in names]

names = ["tom", "richard", "harold"]
names = set(names)

names = ["tom", "richard", "harold"]
names = {name for name in names}

def cube(number):
	return number ** 3

numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(cube, numbers)

for number in cubed_numbers:
	print(number)

print(*cubed_numbers, sep=", ")

def cube(number):
	return number ** 3

numbers = [1, 2, 3, 4, 5]
cubed_numbers = list(map(cube, numbers))

def add(a, b):
	return a + b

odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8, 10]

totals = map(add, odds, evens)
print(*totals, sep=", ")  # 3, 7, 11, 15, 19

numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(lambda number: number ** 3, numbers)

from operator import add

odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8, 10]

totals = map(add, odds, evens)
print(*totals, sep=", ")  # 3, 7, 11, 15, 19


from operator import methodcaller

names = ["tom", "richard", "harold"]
title_names = map(methodcaller("title"), names)

names = ["tom", "richard", "harold"]
title_names = map(lambda name: name.title(), names)

numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = [number for number in numbers if number % 2 == 0]

numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = {number for number in numbers if number % 2 == 0}

numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = filter(lambda number: number % 2 == 0, numbers)

def is_even(number):
	return number % 2 == 0

numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = filter(is_even, numbers)

values = [0, "Hello", [], {}, 435, -4.2, ""]
truthy_values = filter(None, values)

print(*truthy_values, sep=", ") 
