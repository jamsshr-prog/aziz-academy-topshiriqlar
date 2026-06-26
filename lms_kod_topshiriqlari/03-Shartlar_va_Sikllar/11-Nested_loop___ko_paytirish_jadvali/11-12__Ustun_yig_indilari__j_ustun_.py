n, m = map(int, input().split())
sums = [0] * m
for i in range(1, n + 1):
    for j in range(1, m + 1):
        sums[j - 1] += i * j
for total in sums:
    print(total)