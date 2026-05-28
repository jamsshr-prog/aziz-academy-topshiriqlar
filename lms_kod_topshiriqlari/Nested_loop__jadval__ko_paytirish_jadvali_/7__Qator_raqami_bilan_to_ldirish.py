n, m = map(int, input().split())
for i in range(1, n + 1):
    row = [str(i)] * m
    print(" ".join(row))