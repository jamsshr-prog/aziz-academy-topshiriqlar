n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
d2 = {}
for k, v in d.items():
    d2[k] = v * 2
print(d2)