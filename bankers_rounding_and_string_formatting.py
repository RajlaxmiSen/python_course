"""
ceil is the opposite of floor, and ceil always rounds away from zero for positive numbers, but towards zero for negative numbers.

trunc performs truncation, returning the integer portion of a given number.

round implements a type of rounding called bankers' rounding. In bankers' rounding, we round towards the closest significant figure, except in the case of a tie. In the event of a tie, we  round towards the closest even significant figure. So 3.5 rounds to 4, but 2.5 rounds to 2.

floor(-3.1)
trunc(-3.1)
ceil(-5.7)
round(-3.5)
"""


x = 4863.4343091          # example float to format

print(f"{x:.6}")          # f-string version
print("{:.6}".format(x))  # format method version

x1 = 4863.4343091

print(f"{x1:.3}")  # 4.86e+03

x2 = 4863.4343091

print(f"{x2:.3f}")  # 4863.434

x3 = 4863.4343091

print(f"{x3:f}")  # 4863.434309

x4 = 1000000

print(f"{x4:,}")  # 1,000,000
print(f"{x4:_}")  # 1_000_000

questions = 30
correct_answers = 23

print(f"You got {correct_answers / questions :.2%} correct!")
# You got 76.67% correct!
