def rect_area(w, h=1):
    return w * h

nums = list(map(int, input().split()))

if len(nums) == 1:
    print(rect_area(nums[0]))
else:
    print(rect_area(nums[0],nums[1]))