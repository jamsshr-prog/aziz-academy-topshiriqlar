n = int(input())
numbers = list(map(int, input().split()))
summa = 0 
for x in numbers:
    if x > 10:
        summa += x
print(summa)