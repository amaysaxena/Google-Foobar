def answer(x, y):
        return sum(y) - sum(x) if len(y) > len(x) else sum(x) - sum(y)
