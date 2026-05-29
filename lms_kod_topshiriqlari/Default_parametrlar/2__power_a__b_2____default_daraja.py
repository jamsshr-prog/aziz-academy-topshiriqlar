def power(a, b=2):
    return a ** b 

nums = list(map(int, input().split()))

if len(nums) == 1:
    print(power(nums[0]))
else:
    print(power(nums[0], nums[1]))