n = int(input())
lst = list(map(int, input().split()))
result = [x * 2 for x in lst if x > 0]
print(result)