def pack_dict(**kwargs):
    return kwargs

n = int(input())
d = {}

for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
    
print(pack_dict(**d))