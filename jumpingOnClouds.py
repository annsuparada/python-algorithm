# A child is playing a cloud hopping game. In this game, there are sequentially numbered clouds that can be thunderheads or cumulus clouds. The character must jump from cloud to cloud until it reaches the start again.

# There is an array of clouds, c and an energy level e = 100 . The character starts from c[0]  and uses 1 unit of energy to make a jump of size k to cloud c[(i+k) % n]. If it lands on a thundercloud, c[i] = 1, its energy (e) decreases by 2 additional units. The game ends when the character lands back on cloud .

# Given the values of n, k, and the configuration of the clouds as an array c, determine the final value of e after the game ends.

# Function Description

# Complete the jumpingOnClouds function in the editor below.

# jumpingOnClouds has the following parameter(s):

# int c[n]: the cloud types along the path
# int k: the length of one jump
# Returns

# int: the energy level remaining.

def jumpingOnClouds(c, k):
    e = 100
    i = k

    if i == len(c):
        if c[len(c) - 1] == 1:
            return e - 3
        if c[len(c) - 1] == 0:
            return e - 1

    while i != 0:
        e -= 1
        if c[i] == 1:
            e -= 2
        i += k
        if i == len(c):
            if c[0] == 1:
                e -= 3
            if c[0] == 0:
                e -= 1
            i = 0
        if i > len(c):
            reset = i - len(c)
            i = reset

    return e


print(jumpingOnClouds([1, 1, 0, 1, 0, 1,
                       0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1], 19))  # 97

print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0], 2))  # 92
print(jumpingOnClouds([1, 1, 1, 0, 1, 1, 0, 0, 0, 0, ], 3))  # 80
