from __future__ import generators
from fractions import gcd

if 'True' not in globals():
    globals()['True'] = not None
    globals()['False'] = not True

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
    G = graph(banana_list)
    M = matching(G, greedy_matching(G))
    return len(l) - len(M)

class unionFind:

    def __init__(self):
        self.weights = {}
        self.parents = {}

    def __getitem__(self, object):

        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = 1
            return object

        path = [object]
        root = self.parents[object]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        for ancestor in path:
            self.parents[ancestor] = root
        return root

    def union(self, *objects):
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r],r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest

def matching(G, initialMatching = {}):
    matching = {}
    matching = {k:v for k,v in initialMatching.items()}

    def augment():
        leader = unionFind()
        S = {}
        T = {}
        unexplored = []
        base = {}

        def blossom(v,w,a):

            def findSide(v,w):
                path = [leader[v]]
                b = (v,w)
                while path[-1] != a:
                    tnode = S[path[-1]]
                    path.append(tnode)
                    base[tnode] = b
                    unexplored.append(tnode)
                    path.append(leader[T[tnode]])
                return path

            a = leader[a]
            path1,path2 = findSide(v,w), findSide(w,v)
            leader.union(*path1)
            leader.union(*path2)
            S[leader[a]] = S[a]

        topless = object()
        def alternatingPath(start, goal = topless):
            path = []
            while 1:
                while start in T:
                    v, w = base[start]
                    vs = alternatingPath(v, start)
                    vs.reverse()
                    path += vs
                    start = w
                path.append(start)
                if start not in matching:
                    return path
                tnode = matching[start]
                path.append(tnode)
                if tnode == goal:
                    return path
                start = T[tnode]

        def pairs(L):
            i = 0
            while i < len(L) - 1:
                yield L[i],L[i+1]
                i += 2

        def alternate(v):
            path = alternatingPath(v)
            path.reverse()
            for x,y in pairs(path):
                matching[x] = y
                matching[y] = x

        def addMatch(v, w):
            alternate(v)
            alternate(w)
            matching[v] = w
            matching[w] = v

        def ss(v,w):
            if leader[v] == leader[w]:
                return False
            path1, head1 = {}, v
            path2, head2 = {}, w

            def step(path, head):
                head = leader[head]
                parent = leader[S[head]]
                if parent == head:
                    return head
                path[head] = parent
                path[parent] = leader[T[parent]]
                return path[parent]

            while 1:
                head1 = step(path1, head1)
                head2 = step(path2, head2)

                if head1 == head2:
                    blossom(v, w, head1)
                    return False

                if leader[S[head1]] == head1 and leader[S[head2]] == head2:
                    addMatch(v, w)
                    return True

                if head1 in path2:
                    blossom(v, w, head1)
                    return False

                if head2 in path1:
                    blossom(v, w, head2)
                    return False

        for v in G:
            if v not in matching:
                S[v] = v
                unexplored.append(v)

        current = 0
        while current < len(unexplored):
            v = unexplored[current]
            current += 1

            for w in G[v]:
                if leader[w] in S:
                    if ss(v,w):
                        return True

                elif w not in T:
                    T[w] = v
                    u = matching[w]
                    if leader[u] not in S:
                        S[u] = w
                        unexplored.append(u)

        return False

    while augment():
        pass

    return matching


l = [1,3,7,13,19,21]
print(answer(l))