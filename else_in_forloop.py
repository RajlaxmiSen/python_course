# Print whether or a not an integer is prime for all integers from 2 to 100
for dividend in range(2,101):
    divisor = 2

    while dividend >= divisor ** 2:
        result = dividend / divisor
        if result.is_integer():
            print(f"{dividend} is not prime")
            # Break the while loop when a number is proven non-prime
            break
        divisor += 1

    # The else block runs if no break was encountered in the while loop
    else:
        print(f"{dividend} is prime")


"""
Convert the user input to an integer value and check the user's age is
over 18 if the conversion is successful. Otherwise, print an error message.
"""
try:
    age = int(input("Enter your age: "))
except:
    print ("Please only enter numerical characters.")

# The else block only runs if no exception gets raised
else:
    if age < 18:
        print("Sorry, you're too young to watch this movie.")
    else:
        print("Enjoy the movie!")
