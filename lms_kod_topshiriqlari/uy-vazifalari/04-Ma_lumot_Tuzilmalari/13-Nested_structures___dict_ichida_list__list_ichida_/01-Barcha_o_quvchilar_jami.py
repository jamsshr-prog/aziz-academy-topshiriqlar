n = int(input())
jami = 0 
for _ in range(n):
    qator = input().split()
    jami += len(qator) - 1 
print(jami)