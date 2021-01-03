# Function Description

# Complete the extraLongFactorials function in the editor below. It should print the result and return.

# extraLongFactorials has the following parameter(s):

# n: an integer

def extraLongFactorials(n):
    result = 1
    # iterate through range 1 to n
    for i in range(1, n + 1):
        result *= n
        n -= 1

    return result


print(extraLongFactorials(25))  # 15511210043330985984000000
