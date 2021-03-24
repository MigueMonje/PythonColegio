def listmult(a,l):
    for i in l:
        if a % i ==0:
            return True
    return False
def funclist(l,func):
    return [func(i) for i in l]
primes = []
upto = int(input(">> "))
for i in range(upto):
    if i > 1:
        if not listmult(i,primes):
            primes += [i]
print("\n".join(funclist(primes,str)))
