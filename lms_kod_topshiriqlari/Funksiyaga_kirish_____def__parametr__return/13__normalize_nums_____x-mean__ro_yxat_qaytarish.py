def normalize(nums):
    mean = sum(nums) / len(nums)
    return [x - mean for x in nums]
nums = list(map(int, input().split()))
result = normalize(nums)
print(*[f"{x:.2f}" for x in result])