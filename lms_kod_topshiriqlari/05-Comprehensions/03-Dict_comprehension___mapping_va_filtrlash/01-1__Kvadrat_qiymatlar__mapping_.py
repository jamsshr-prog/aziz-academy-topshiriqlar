n = int(input())
d= {} 
for _ in range (n):
    key, val = input().split()
    d[key] = int(val)
result = {k: v**2 for k, v in d.items()}
print(result)