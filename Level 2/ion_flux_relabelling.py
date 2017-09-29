two_raised_to  = {0: 1, 1: 2, 2: 4, 3: 8, 4: 16, 5: 32, 6: 64, 7: 128, 8: 256, 9: 512, 10: 1024, 11: 2048, 12: 4096, 13: 8192, 14: 16384, 15: 32768, 16: 65536, 17: 131072, 18: 262144, 19: 524288, 20: 1048576, 21: 2097152, 22: 4194304, 23: 8388608, 24: 16777216, 25: 33554432, 26: 67108864, 27: 134217728, 28: 268435456, 29: 536870912, 30: 1073741824}

def answer(h, q):
    return [find_parent(two_raised_to[h] - 1, h, x) for x in q]

def find_parent (root, h, x):
    left = root - two_raised_to[h-1]
    right = root - 1

    if x in {left, right}:
        return root

    elif (x > left) :
        return find_parent(right, h-1, x)

    return find_parent(left, h-1, x)


height = 30
print(find_parent(two_raised_to[height] - 1, height, 11))
