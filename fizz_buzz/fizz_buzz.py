MAX = 50

"""
print integers one-to-N
but print "Fizz" if the integer is divisible by 3
print "Buzz" if the integer is divisible by 5
print "FizzBuzz" if the integer is divisible by both 3 and 5
"""

for num in range(1, MAX+1):
    if num % 5 == 0 and num % 3 == 0 : print("FizzBuzz")
    elif num % 3 == 0 : print("Fizz")
    elif num % 5 == 0 : print("Buzz")
    else : print(num)