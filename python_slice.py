slice_instance = slice(0, 2)
print(type(slice_instance))

x = [1, 2, 3, 4, 5]
x_slice = x[slice_instance]
print(x_slice)  # [1, 2]

"""
x_slice is of type list.
The item at index 2 of x wasn't included in x_slice.
"""

s = slice(1, 4)

t = (1, 2, 3, 4, 5)  # tuple
l = [1, 2, 3, 4, 5]  # list
c = "12345"          # string

print(t[s])  # (2, 3, 4)
print(l[s])  # [2, 3, 4]
print(c[s])  # 234

t = (1, 2, 3, 4, 5)
print(t[slice(1, 4)])  # (2, 3, 4)

t = (1, 2, 3, 4, 5)
print(t[1:4])  # (2, 3, 4)

print(t[:4]) 
print(t[1:]) # the final element is included in the new slice
print(t[:]) # you get everything back

# Using step values

t = (1, 2, 3, 4, 5)
print(t[1:4:2])  # (2, 4)

# When a step value is negative, we start at the starting index as usual, but then move along the sequence in reverse.

t = (1, 2, 3, 4, 5)
print(t[4:0:-1]) 
#Notice that the results came back in the reverse order to the original tuple. This is because the values at the end of the tuple were encountered first, and we kept stepping towards the start of the tuple.

t = (1, 2, 3, 4, 5)
print(t[1:4:-1]) 

t = (1, 2, 3, 4, 5)
print(t[-1:-5:-1])  # (5, 4, 3, 2)
