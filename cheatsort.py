import random
def cheatsort(l):
    mn = l[0]
    mx = 0
    data = {}
    for e in l:
        if not (e in data):
            data[e] = 0
        data[e] += 1
        if e > mx:
            mx = e
        elif e < mn:
            mn = e
    result = []
    for i in range(mn,mx+1):
        if i in data:
            result += [i]*data[i]
    return result
randlist = [random.randint(1,1000) for _ in range(1000)]
print(randlist)
sortlist = cheatsort(randlist)
print(sortlist)