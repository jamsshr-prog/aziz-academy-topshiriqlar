n = int(input().strip())
d = {} 
for _ in range(n):
    k, v = input().split()
    if k not in d:
        d[k] = int(v)
print(min(d, key=d.get))