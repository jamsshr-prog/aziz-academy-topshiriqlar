nums = [int(x) for x in input().split()]
abs_nums = {abs(x) for x in nums}
print(*sorted(abs_nums))