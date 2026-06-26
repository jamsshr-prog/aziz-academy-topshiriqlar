n = int(input())
numbers = list(map(int, input().split()))
max_num = numbers[0]
min_num = numbers[0]
for x in numbers:
    if x > max_num:
        max_num = x
    if x < min_num:
        min_num = x
print(max_num - min_num)   