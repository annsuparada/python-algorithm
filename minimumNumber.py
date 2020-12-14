# Louise joined a social networking site to stay in touch with her friends. The signup page required her to input a name and a password. However, the password must be strong. The website considers a password to be strong if it satisfies the following criteria:

# Its length is at least .
# It contains at least one digit.
# It contains at least one lowercase English character.
# It contains at least one uppercase English character.
# It contains at least one special character. The special characters are: !@#$%^&*()-+
# She typed a random string of length  in the password field but wasn't sure if it was strong. Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

# Note: Here's the set of types of characters in a form you can paste in your solution:
# numbers = "0123456789"
# lower_case = "abcdefghijklmnopqrstuvwxyz"
# upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# special_characters = "!@#$%^&*()-+"

# Function Description

# Complete the minimumNumber function in the editor below.

# minimumNumber has the following parameters:

# int n: the length of the password
# string password: the password to test
# Returns

# int: the minimum number of characters to add


def minimumNumber(n, password):

    minNum = 0
    txt = "!@#$%^&*()-+"

    if n <= 3:
        return 6 - n

    count = {"number": 0, "lower": 0, "upper": 0, "special": 0}

    for i in password:
        # x = re.search(i, txt)
        if i.isnumeric():
            count['number'] = count["number"] + 1
        if i.islower():
            count["lower"] = count["lower"] + 1
        if i.isupper():
            count["upper"] = count["upper"] + 1
        for j in txt:
            if i == j:
                count["special"] = count["special"] + 1

    for i in count.values():
        if i == 0:
            minNum += 1

    checkLen = minNum + n
    the_rest = 6 - checkLen
    if checkLen < 6:
        return minNum + the_rest

    return minNum


# print(minimumNumber(4, '4700'))  # 3
# print(minimumNumber(4, 'goxg'))  # 3
# print(minimumNumber(5, '55542'))  # 3
# print(minimumNumber(7, "4#!Y09"))  # 0
# print(minimumNumber(1, "4"))  # 5
# print(minimumNumber(11, "#HackerRank"))  # 1
# print(minimumNumber(4, "&+^&"))  # 3
print(minimumNumber(4, "1z2!"))  # 2
