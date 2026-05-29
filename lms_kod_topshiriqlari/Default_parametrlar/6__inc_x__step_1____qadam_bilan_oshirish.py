def inc(x, step=1):
    return x + step

print(inc(*map(int, input().split())))