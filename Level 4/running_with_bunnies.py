from itertools import chain, combinations, permutations

def answer(times, time_limit):
    if len(times) <= 2:
        return []
    n = len(times)
    bunny_ids = list(range(n - 2))
    shortest_dist = floyd_warshall(times)

    if negative_cycle(shortest_dist):
        # Negative cycle found. Save all the bunnies!
        return bunny_ids

    optimal_bunnies = []
    # Check each subset of the bunny_ids by brute force to find
    # optimal sequence
    ps = sorted(powerset(bunny_ids))
    for s in ps:
        for sequence in permutations(s):
            if path_length(sequence, shortest_dist) <= time_limit:
                if len(sequence) > len(optimal_bunnies):
                    optimal_bunnies = list(s)
                    if len(optimal_bunnies) == n - 2:
                        break
    return optimal_bunnies


# Helper function that, when given a sequence of bunny ids and the result
# of floyd warshall, returns the time cost of going from start, picking up each
# bunny in @param sequence, and then extiting from the gate.

def path_length(sequence, shortest_dist):
    bunny_indices = [id + 1 for id in sequence]
    # This is the path taken. starts from starting point (index 0), then
    # goes through the sequence of bunnies, and finally ends at the gate.
    indices_to_visit = [0] + bunny_indices + [len(shortest_dist) - 1]

    # Sum the lengths of each arc. sum = dist(node0, node1) + dist(node1, node2) ... dist(nodeN-1, nodeN)
    return sum([shortest_dist[indices_to_visit[i]][indices_to_visit[i+1]]
               for i in range(len(indices_to_visit) - 1)])

# Floyd-Warshall algorithm for finding length of shortest paths between
# each index.
def floyd_warshall(times):
    n = len(times)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if times[i][k] + times[k][j] < times[i][j]:
                    times[i][j] = times[i][k] + times[k][j]
    return times

# Detect negative cycles in teh result of floyd-warshall.
def negative_cycle(times):
    return any([times[i][i] < 0 for i in range(len(times))])

# Helper method to compute the power set of a list of indices.
def powerset(iterable):
    # s = list(iterable)
    # return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    x = len(iterable)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, iterable) if i & mask]

print(sorted(powerset([1,2,3,4])))

print(answer(
    [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],
    1
))