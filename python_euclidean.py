def euclidean_division(x, y):
	quotient = x // y
	remainder = x % y
	print(f"{quotient} remainder {remainder}")

euclidean_division(-10, 3)
euclidean_division(10, -3)

'''
Floor division always rounds away from zero for negative numbers, so -3.5 will round to -4, but towards zero for positive numbers, so 3.5 will round to 3.
Floor division and modulo are linked by the following identity, x = (x // y) * y + (x % y), which is why modulo also yields unexpected results for negative numbers, not just floor division.
'''
