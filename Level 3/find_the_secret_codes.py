def answer(l):
    n = len(l)
    c = [0] * n
    triples = 0
    for k in range(n):
        for j in range(k):
            if l[k] % l[j] == 0:
                c[k] += 1
                triples += c[j]
    return triples


l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,25,100000]
print(answer(l))
