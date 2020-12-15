# In this challenge, you will be given a string. You must remove characters until the string is made up of any two alternating characters. When you choose a character to remove, all instances of that character must be removed. Your goal is to create the longest string possible that contains just two alternating letters.

# As an example, consider the string abaacdabd. If you delete the character a, you will be left with the string bcdbd. Now, removing the character c leaves you with a valid string bdbd having a length of 4. Removing either b or d at any point would not result in a valid string.

# Given a string , convert it to the longest possible string  made up only of alternating characters. Print the length of string  on a new line. If no string  can be formed, print  instead.

# Function Description

# Complete the alternate function in the editor below. It should return an integer that denotes the longest string that can be formed, or  if it cannot be done.

# alternate has the following parameter(s):

# s: a string

def alternate(s):
    char = set()
    pair_s = []
    new_s = set()
    maxNum = 0

    for i in s:
        char.add(i)

    for i in char:
        for j in char:
            if j != i:
                pair_s.append([i, j])

    for i in pair_s:
        temp_s = ""
        for j in range(0, len(s)):

            if s[j] == i[0] or s[j] == i[1]:
                temp_s += s[j]
        new_s.add(temp_s)

    valid_s = new_s.copy()
    for i in new_s:
        for j in range(0, len(i)):
            if j > 0 and i[j] == i[j - 1]:
                valid_s.discard(i)

    if len(valid_s) == 0:
        return 0

    for i in valid_s:
        if len(i) > maxNum:
            maxNum = len(i)

    return maxNum


print(alternate('beabeefeab'))  # 5
print(alternate('asdcbsdcagfsdbgdfanfghbsfdab'))  # 8
print(alternate('asvkugfiugsalddlasguifgukvsa'))  # 0
