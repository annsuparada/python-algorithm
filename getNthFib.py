def getNthFib(n):
    fib = [0, 1]
    if n == 1:
        return fib

    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


print(getNthFib(6))  # [0,1,1,2,3,5]
