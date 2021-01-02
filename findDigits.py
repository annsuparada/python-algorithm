# An integer d is a divisor of an integer n if the remainder of n % d = 0 .

# Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer.

# Function Description

# Complete the findDigits function in the editor below.

# findDigits has the following parameter(s):

# int n: the value to analyze
# Returns

# int: the number of digits in n that are divisors of n

def findDigits(n):
    result = 0
    s = str(n)

    for i in s:
        num = int(i)
        if num != 0:
            d = n % num
            if d == 0:
                result += 1

    return result


print(findDigits(12))  # 2
print(findDigits(1012))  # 3
