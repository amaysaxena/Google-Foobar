true, false = True, False

PREV_STATES2 = {0: ((0, 0),
                    (1, 1),
                    (0, 3),
                    (1, 2),
                    (1, 3),
                    (2, 1),
                    (3, 0),
                    (3, 1),
                    (2, 2),
                    (2, 3),
                    (3, 2),
                    (3, 3)),
                1: ((2, 0),
                    (0, 2),
                    (1, 0),
                    (0, 1))}

NEXT_STATES2 = zeros = [ [0]*4 for _ in range(4) ]
NEXT_STATES2[2][0] = 1
NEXT_STATES2[0][2] = 1
NEXT_STATES2[1][0] = 1
NEXT_STATES2[0][1] = 1


def check_overlap(int_pair_prev, int_pair_next):
    check1 = int_pair_prev[0] % 2 == int(int_pair_next[0] > 1)
    check2 = int_pair_prev[1] % 2 == int(int_pair_next[1] > 1)
    return check1 and check2

def append_bits(partial_soln, nums_to_append):
    result1 = (partial_soln[0] << 1) + (nums_to_append[0] % 2)
    result2 = (partial_soln[1] << 1) + (nums_to_append[1] % 2)
    return (result1, result2)

def column_k(g, k, r=-1):
    if r == -1:
        return tuple([g[i][k] for i in range(len(g))])
    return tuple([g[i][k] for i in range(r)])

def next_state(column_pair, m):
    col_1 = column_pair[0]
    col_2 = column_pair[1]
    result = 0
    for i in range(m - 1):
        int1 = col_1 % 4
        int2 = col_2 % 4
        next_result = NEXT_STATES2[int1][int2]
        result = (next_result << i) + result
        col_1, col_2 = (col_1 >> 1), (col_2 >> 1)
    return result
#
# def print_base_2(integer, m):
#     result = ''
#     for _ in range(m - 1):
#         result += str(integer % 2)
#         integer = integer >> 1
#     return result[::-1]

def past_states(col, m):
    for i in range(1 << (m + 1)):
        for j in range(1 << (m + 1)):
            if next_state((i, j), m + 1) == col:
                yield (i, j)

def past_states2(col):
    col = [int(b) for b in col]
    m = len(col)
    first_past_states = PREV_STATES2[col[0]]
    fringe = [(s, 0) for s in first_past_states]
    while len(fringe) != 0:
        partial_solution = fringe.pop()
        k = partial_solution[1]
        if k == m - 1:
            yield partial_solution[0]
        else:
            bool = col[k + 1]
            valid_past_states = (s for s in PREV_STATES2[bool] if check_overlap(partial_solution[0], s))
            for valid_state in valid_past_states:
                next_partial_solution = append_bits(partial_solution[0], valid_state)
                fringe.append((next_partial_solution, k + 1))

def array_to_ints(col):
    result = 0
    for bit in col:
        result = (result << 1) + int(bit)
    return result

# print(past_states(0, 9))
# print(next_state((0, 1), 100))

def answer(g):
    first_col = column_k(g, 0)
    m, n = len(g), len(g[0])
    # if m > n:
    #     g = [[row[i] for row in g] for i in range(len(g[0]))]
    #     m, n = n, m

    g = [array_to_ints(column_k(g, i)) for i in range(n)]
    # dp = {}

    dp = [[0] * (1 << (m + 1)) for _ in range(n)]

    for a, b in past_states2(first_col):
        dp[0][b] += 1

    for i in range(1, n):
        for j in range(1 << (m + 1)):
            for k in range(1 << (m + 1)):
                if(check(j, k, g, i, m)):
                    dp[i][k] += dp[i - 1][j]
    return sum(dp[n - 1])


    # def answer_recursive(index, last_col):
    #     if index == n:
    #         return 1
    #
    #     if (index, last_col) in dp:
    #         return dp[(index, last_col)]
    #
    #     result = 0
    #     for possible_next_col in range(1 << (m + 1)):
    #         if check(last_col, possible_next_col, g, index, m):
    #             result += answer_recursive(index + 1, possible_next_col)
    #     dp[(index, last_col)] = result
    #     return result
    #
    # result = 0
    # for starting_col in past_states2(first_col):
    #     result += answer_recursive(1, starting_col[1])
    # return result

def check(last_col, possible_next_col, g, index, m):
    return next_state((last_col, possible_next_col), m + 1) == g[index]


g1 = [
    [true, false, true],
    [false, true, false],
    [true, false, true]
]
# expect: 4

g2 = [
    [true, false, true, false, false, true, true, true],
    [true, false, true, false, false, false, true, false],
    [true, true, true, false, false, false, true, false],
    [true, false, true, false, false, false, true, false],
    [true, false, true, false, false, true, true, true]
]
# expect 254

g3 = [[true, true, false, true, false, true, false, true, true, false],
     [true, true, false, false, false, false, true, true, true, false],
     [true, true, false, false, false, false, false, false, false, true],
     [false, true, false, false, false, false, true, true, false, false]]

# expect 11567

print(answer(g2))





#
#
# def past_states2(col):
#     col = [int(b) for b in col]
#     m = len(col)
#     first_past_states = PREV_STATES2[col[0]]
#     fringe = [(s, 0) for s in first_past_states]
#     solutions = set()
#     while len(fringe) != 0:
#         partial_solution = fringe.pop()
#         k = partial_solution[1]
#         if k == m - 1:
#             solutions |= {partial_solution[0]}
#         else:
#             bool = col[k + 1]
#             valid_past_states = (s for s in PREV_STATES2[bool] if check_overlap(partial_solution[0], s))
#             for valid_state in valid_past_states:
#                 next_partial_solution = append_bits(partial_solution[0], valid_state)
#                 fringe.append((next_partial_solution, k + 1))
#     return solutions
#
#
#
# def answer(g):
#     num_paths_prev = {}
#     num_paths_curr = {}
#     col_cache = {}
#
#     for i in range(len(g)):
#         col = column_k(g, i)
#
#         if len(num_paths_prev) == 0:
#             for column_sol in past_states2(col):
#                 if column_sol in num_paths_curr:
#                     num_paths_curr[column_sol] += 1
#                 else:
#                     num_paths_curr[column_sol] = 1
#
#         else:
#             if col in col_cache:
#                 current_predeccessors = col_cache[col]
#             else:
#                 current_predeccessors = past_states2(col)
#                 col_cache[col] = current_predeccessors
#
#             for column_sol in current_predeccessors:
#                 for prev_solution in num_paths_prev:
#                     if column_sol[0] == prev_solution[1]:
#                         if column_sol in num_paths_curr:
#                             num_paths_curr[column_sol] += num_paths_prev[prev_solution]
#                         else:
#                             num_paths_curr[column_sol] = num_paths_prev[prev_solution]
#
#         num_paths_prev = num_paths_curr
#         num_paths_curr = {}
#
#     return sum(num_paths_prev.values())
#
#
#
#
