"""
String interpolation

Question : why 0 is {file_number:03} : ans : 0 is filling the place only
suppose if you don't pass 0 the it will replace 0 with space
"""

# normal process

# number_of_files = 3

# for file_number in range(1, number_of_files + 1):
# 	print(f"image{file_number:03}.png")

# nested process
number_of_files = 10
number_digits = int(input("How many digits are used in the numbering scheme? "))

for file_number in range(1, number_of_files + 1):
	print(f"image{file_number:{number_digits}}.png")
#Nested string interpolation with format
number_of_files = 3
number_digits = int(input("How many digits are used in the numbering scheme? "))

for file_number in range(1, number_of_files + 1):
	print("image{:0{}}.png".format(file_number, number_digits))

####################
number_of_files = 3
number_digits = int(input("How many digits are used in the numbering scheme? "))

for file_number in range(1, number_of_files + 1):
	print("image{number:0{padding_amount}}.png".format(
		number=file_number,
		padding_amount=number_digits
	))
	
	
#base code
base_10 = 231

print(f"This is the number in binary: {base_10 :b}")
# This is the number in binary: 11100111

base_10 = 231

print(f"This is the number in octal: {base_10 :o}")
# This is the number in octal: 347

print(f"This is the number in hexadecimal: {base_10 :x}")
# This is the number in hexadecimal: e7

print(f"This is the number in uppercase hexadecimal: {base_10 :X}")

base_16 = int("E7", base=16)
    
print(f"This is the number in decimal: {base_16 :d}")

