def slice_text(s, start=0, end=None):
    return s[start:end]

s = input()
nums = input().split()

if len(nums) == 0:
    print(slice_text(s))
elif len(nums) == 1:
    print(slice_text(s, int(nums[0])))
else:
    print(slice_text(s, int(nums[0]), int(nums[1])))
