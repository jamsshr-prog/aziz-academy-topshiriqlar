n = int(input().strip())
d = {} 
for _ in range(n):
    line = input().strip().split()
    name = line[0]
    score = int(line[1])
    d[name] = score
print(sum(d.values()))