def primlenakr(k,a,b):
    kr = k**2
    prim = a*b
    return prim * kr
def sortirovka(a):
    a = sorted(a)
    return a
def maxChislo(a):
    a = sortirovka(a)
    a = a[len(a)-1]
    return a