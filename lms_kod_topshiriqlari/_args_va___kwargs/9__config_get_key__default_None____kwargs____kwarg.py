word = input()
n = int(input())

result = 0

for i in range(n):
    w, nums = input().split()
    nums = int(nums)
    
    if w == word:
        result = nums
        
print(result)