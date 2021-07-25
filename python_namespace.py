print(globals())

names = ["Mike", "Fiona", "Patrick"]
x = 53657

def add(a, b):
	print(a, b)

print(globals())

#locals
def add(a, b):
	print(locals())
	print(a, b)

add(7, 25)

####
def greet(name):
	print(locals())
	greeting = f"Hello, {name}!"
	print(locals())
	print(greeting)

greet("Phil")

## getting value out of function
def add(a, b):
	return a + b

result = add(5, 12)
print(result)  # 1

##### if we don't return anything then it return none
def greet(name):
	greeting = f"Hello, {name}!"
	print(greeting)

print(greet('Phil'))
