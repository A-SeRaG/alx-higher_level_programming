#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod = number % 10 if number > 0 else number % -10
print("Last digit of {:d}".format(number), end="")
if mod > 5:
    print(" is {:d} and is greater than 5".format(mod)
elif mod < 5 and number != 0:
    print(" is {:d} and is less than 6 and not 0".format(mod))
else:
    print(" is 0 and is 0")
