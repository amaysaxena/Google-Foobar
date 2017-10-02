from fractions import gcd

is_power_of_two = lambda k : bool(not (k & (k-1)) and k)
loops = lambda a,b : not is_power_of_two((a+b)//gcd(a,b))

def graph(l):
    G = {}
    for i in range(len(l)):
        G[i] = set(filter(lambda j: loops(l[i], l[j]), range(len(l))))
    return G

def greedy_matching(G):
    deg = lambda v: len(G[v])
    vertices = sorted(list(range(len(G))), key=deg)
    matching = {}
    for v in vertices:
        if v not in matching:
            for w in G[v]:
                if w not in matching:
                    matching[v] = w
                    matching[w] = v
                    break
    return matching

def answer(banana_list):
    M = greedy_matching(graph(banana_list))
    return len(l) - len(M)



l = [1,3,7,13,19,21]
print(graph(l))
print(greedy_matching(graph(l)))
print(answer(l))



