def min_max(nums):
    return (min(nums), max(nums))
nums = list(map(int, input().split()))
mn, mx = min_max(nums)
print(mn)
print(mx)