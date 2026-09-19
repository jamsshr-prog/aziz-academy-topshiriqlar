n = int(input().strip())
d = {} 
for i in range(n):
    d[f"k{i}"] = int(input().strip())
print(sum(d.values()))