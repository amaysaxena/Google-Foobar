def answer(n):
    lst = range(1, n)
    buffer = [0] * (n + 1)
    buffer[0] = 1
    for x in lst:
        for y in range(n, x - 1, -1):
            if buffer[y - x]:
                buffer[y] += buffer[y - x]
    return buffer[n]

print(answer(200))