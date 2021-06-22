euclidean_divison = divmod(5, 2)
print(euclidean_divison)  # (2, 1)
quotient, remainder = divmod(5, 2)
print(quotient)
print(remainder)

print(divmod(5.5, 2))  # (2.0, 1.5)
print(divmod(6.0, 2))  # (3.0, 0.0)

############## hour min sec
raw_time = 8594

minutes, seconds = divmod(raw_time, 60)
hours, minutes = divmod(minutes, 60)

print(f"{raw_time}s is {hours}h {minutes}m {seconds}s")
# 8594s is 2h 23m 14s
