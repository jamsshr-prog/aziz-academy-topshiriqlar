n = int(input())
d = {} 
for _ in range(n):
    key, val = input().split()
    d[key] = int(val)
result = {
    k: (v * 3 if v % 2 != 0 else v * 2)
    for k, v in d.items()
    if abs(v) >= 2
}
print(result)