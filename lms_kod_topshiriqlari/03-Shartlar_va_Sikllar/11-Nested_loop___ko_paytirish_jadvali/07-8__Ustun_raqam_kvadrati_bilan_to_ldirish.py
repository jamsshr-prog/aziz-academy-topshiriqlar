n, m = map(int, input().split())
for son in range(n, m + 1):
    if son > n:
        print(" ", end="")
    print(son * son, end="")