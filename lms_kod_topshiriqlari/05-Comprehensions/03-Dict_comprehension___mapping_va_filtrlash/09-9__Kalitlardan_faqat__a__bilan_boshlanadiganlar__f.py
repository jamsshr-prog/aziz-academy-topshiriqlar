n = int(input())
d = {}
for _ in range(n):
    key, val = input().split()
    d[key] = int(val)
result = {k: v for k, v in d.items() if k.startswith('a')}
print(result)