nums = [int(x) for x in input().split()]
unique_nums = {x for x in nums}
print(*sorted(unique_nums))