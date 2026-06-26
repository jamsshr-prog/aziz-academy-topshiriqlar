n = int(input())
d = {} 
for _ in range(n):
    key, val = input().split()
    d[key] = int(val)
result = {k: abs(v) for k, v in d.items() if abs(v) >= 5}
print(result)