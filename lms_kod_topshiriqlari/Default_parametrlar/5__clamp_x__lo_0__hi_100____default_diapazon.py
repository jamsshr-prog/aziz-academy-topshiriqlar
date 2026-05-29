def clamb(x, lo=0, hi=100):
    return max(lo, min(x, hi))

print(clamb(*map(int, input().split())))