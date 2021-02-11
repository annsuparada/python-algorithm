def appendAndDelete(s, t, k):
    sCounter = 0
    tCounter = 0
    newT = t + "." * len(s)
    sLength = len(s)
    if len(s) < len(t):
        s = s + "." * len(t)

    for i in range(0, len(s)):
        # print(s[i], newT[i], 'i:', i)
        if s[i] != newT[i]:
            # print('test')
            sCounter = i + 1
            tCounter = i + 1
            break

    # print(sCounter, tCounter)
    if sCounter > 0 and tCounter > 0:
        sCounter = sLength - sCounter
        tCounter = len(t) - tCounter
    # if sCounter < 0 or tCounter < 0:
    #     return 'No'
    numChar = sCounter + tCounter
    # print(sCounter, tCounter)
    # print('numChar', numChar)
    if numChar <= k:
        return 'Yes'
    else:
        return 'No'


print(appendAndDelete('asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv',
                      'asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv', 20))  # Yes
print(appendAndDelete('aaaaaaaaaa', 'aaaaa', 7))  # Yes
print(appendAndDelete('zzzzz', 'zzzzzzz', 4))  # Yes
print(appendAndDelete('asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv',
                      'bsdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv', 100))  # No
print(appendAndDelete('y', 'yu', 2))  # No

print(appendAndDelete('ashley', 'ash', 2))  # No
