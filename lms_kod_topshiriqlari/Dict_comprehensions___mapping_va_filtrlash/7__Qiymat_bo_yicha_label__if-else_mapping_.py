n = int(input())
d = {} 
for _ in range(n):
    key, val = input().split()
    d[key] = int(val)
result = {k: 'even' if v % 2 == 0 else 'odd' for k, v in d.items()}
print(result)