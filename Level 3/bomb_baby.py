def answer(M, F):
    M, F = int(M), int(F)
    i = 0
    while (M,F) != (1,1):
        _max = max(M,F)
        _min = min(M,F)
        _mod = _max%_min
        if _min == 1:
            return str(i + (_max - 1))
        elif _mod == 0:
            return "impossible"
        i += _max // _min
        M, F = _mod, _min
    return str(i)


print(answer(20,21))