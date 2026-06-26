n = int(input())
numbers = list(map(int, input().split()))
total = 0
for x in numbers:
    if x > 0:
        total += x
print(total)