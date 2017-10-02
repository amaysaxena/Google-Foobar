import numpy as np
import itertools

def answer(g):
    return 3

def column_k(g, k):
    return [g[i][k] for i in range(len(g))]

def next_state(col):
    result = []
    for i in range(len(col) - 1):
        result.append(int(sum(int(k) for k in col[i] + col[i + 1]) == 1))
    return result

def all_states(m):
    for l in itertools.product([0, 1], repeat=2*(m+1)):
        l = np.array(l)
        yield list(np.reshape(l, (m+1, 2)))

def past_states(curr_state):
    m = len(curr_state)
    return (k for k in all_states(m) if next_state(k) == curr_state)

print(list(past_states([1, 0, 1, 1, 0, 0, 0, 0])))
print(list(all_states(4)))

print(next_state(
    [
        [0,1],
        [0,0],
        [0,0],
        [1,0],
        [0,0],
        [1,1],
        [1,0],
        [1,1],
        [1,0]
    ]
))

