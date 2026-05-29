def clamb(x, lo, hi):
    if x < lo:
        return lo
    elif x > hi:
        return hi
    else:
        return x
    
x, lo, hi = map(int, input().split())

print(clamb(x, lo, hi))
print(clamb(lo=lo, hi=hi, x=x))