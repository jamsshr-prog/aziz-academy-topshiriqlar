n = int(input())
numbers = list(map(int, input().split()))
total = 0
for x in numbers:
    total += x
average = total / n
print(average)