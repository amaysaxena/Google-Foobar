PREV_STATES = {0: (((0, 0), (0, 0)), ((0, 0), (1, 1)), ((0, 1), (0, 1)), ((0, 1), (1, 0)), ((0, 1), (1, 1)), ((1, 0), (0, 1)), ((1, 0), (1, 0)), ((1, 0), (1, 1)), ((1, 1), (0, 0)), ((1, 1), (0, 1)), ((1, 1), (1, 0)), ((1, 1), (1, 1))),
               1: (((1, 0), (0, 0)), ((0, 1), (0, 0)), ((0, 0), (1, 0)), ((0, 0), (0, 1)))}

'''
    For a given pair of columns, this function finds the unique column that is
    the image of the grid formed by stacking col1 and col2 under the evolution
    rule of this cellular automata.
'''
def get_successor(col1, col2):
    return [int(sum(col1[i:i+2] + col2[i:i+2]) == 1) for i in range(len(col1) - 1)]


'''
    Given a column, and a target image, this function returns a list of all
    columns that, when stacked on top of last_col, would produce the image
    target, under the evolution rule of this cellular automata.
'''
def next_valid_columns(last_col, target):
    first_successor_value = target[0]
    fringe = []
    for x in range(2):
        for y in range(2):
            if get_successor(last_col[:2], (x,y))[0] == first_successor_value:
                fringe.append((x, y))

    while(len(fringe) > 0):
        partial_solution = fringe.pop()

        if (len(partial_solution) == len(last_col)):
            yield partial_solution
        else:
            target_index = len(partial_solution) - 1
            current_successor_value = target[target_index]
            for possible_next_bool in range(2):
                possible_partial_solution = partial_solution + (possible_next_bool, )
                if get_successor(last_col[target_index: target_index + 2], possible_partial_solution[-2:])[-1] == current_successor_value:
                    fringe.append(possible_partial_solution)


'''
    Given a target column, this function returns all possible 2 x (m+1)
    preimages of the target. This is called only once in answer(g), in order
    to ccompute the predeccessors of the very first column.
'''
def all_predeccessors(target):
    fringe = []
    for predeccessor in PREV_STATES[target[0]]:
        fringe.append(predeccessor)

    while(len(fringe) > 0):
        partial_solution = fringe.pop()

        if (len(partial_solution[0]) == len(target) + 1):
            yield partial_solution
        else:
            target_index = len(partial_solution[0]) - 1
            current_successor_value = target[target_index]

            valid_past_states = (s for s in PREV_STATES[current_successor_value] if s[0]==(partial_solution[0][-1], partial_solution[1][-1]))
            for past_state in valid_past_states:
                new_partial_sol_column1 = partial_solution[0] + (past_state[1][0], )
                new_partial_sol_column2 = partial_solution[1] + (past_state[1][1], )
                new_partial_solution = (new_partial_sol_column1, new_partial_sol_column2)
                fringe.append(new_partial_solution)

'''
    Find and return the number of possible preimages of grid g.
    We do this by maintaining two dictionaries. Both dictionaries have
    a similar form, where dict[COLUMN] is the total number of partial
    solutions found so far that end with COLUMN.
'''
def answer(g):
    # Clean up g. If g has more rows than columns, we use the transpose of g instead
    m, n = len(g), len(g[0])
    if m < n:
        g = [[row[i] for row in g] for i in range(len(g[0]))]
    for i in range(len(g)):
        g[i] = list(map(int, g[i]))

    num_paths_last_col = {}
    first_column = g[0]
    for predeccessor in all_predeccessors(first_column):
        if predeccessor[1] in num_paths_last_col:
            num_paths_last_col[predeccessor[1]] += 1
        else:
            num_paths_last_col[predeccessor[1]] = 1

    for column in g[1:]:
        num_paths_current_col = {}
        for last_col in num_paths_last_col:
            for valid_column in next_valid_columns(last_col, column):
                if valid_column in num_paths_current_col:
                    num_paths_current_col[valid_column] += num_paths_last_col[last_col]
                else:
                    num_paths_current_col[valid_column] = num_paths_last_col[last_col]
        num_paths_last_col = num_paths_current_col
    return sum(num_paths_last_col.values())
