def answer(l):
    factors = [0] * len(l)
    triples = 0
    for k in range(len(l)):
        for j in range(k):
            if l[k] % l[j] == 0:
                factors[k] += 1
                triples += factors[j]
    return triples


l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,25,100000]
print(answer(l))
