n = int(input())
d = {} 
for _ in range(n):
    key, val = input().split()
    d[key] = int(val)
X = int(input())
result = {k: v for k, v in d.items() if v >= X}
print(result)