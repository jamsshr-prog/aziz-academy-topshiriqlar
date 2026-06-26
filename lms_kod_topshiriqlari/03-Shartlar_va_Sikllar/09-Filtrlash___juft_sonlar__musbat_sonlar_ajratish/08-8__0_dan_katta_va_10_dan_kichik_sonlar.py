n = int(input())
numbers = list(map(int, input().split()))
for x in numbers:
    if 0 < x < 10:
        print(x)