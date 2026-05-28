n = int(input())
numbers = list(map(int, input().split()))
sum_even = 0
for x in numbers:
    if x % 2 == 0:
        sum_even += x
print(sum_even)