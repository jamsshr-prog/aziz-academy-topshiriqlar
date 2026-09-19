n = int(input().strip())
d = {}
for _ in range(n):
    word = input().strip()
    d[word] = True
print(len(d))