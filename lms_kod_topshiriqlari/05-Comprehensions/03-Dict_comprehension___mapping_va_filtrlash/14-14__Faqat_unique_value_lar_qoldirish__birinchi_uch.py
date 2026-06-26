n = int(input())
d = {} 
for _ in range(n):
    key, val = input().split()
    d[key] = int(val)
seen_values = set()
result = {}
for k, v in d.items():
    if v not in seen_values:
        seen_values.add(v)
        result[k] = v
print(result)