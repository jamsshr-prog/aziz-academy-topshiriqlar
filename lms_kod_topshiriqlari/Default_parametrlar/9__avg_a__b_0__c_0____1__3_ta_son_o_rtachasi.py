def avg(a, b=0, c=0):
    return (a+b+c) / (1 + (b!=0) + (c!=0))

x = list(map(int, input().split()))
print(f"{avg(*x):.2f}")