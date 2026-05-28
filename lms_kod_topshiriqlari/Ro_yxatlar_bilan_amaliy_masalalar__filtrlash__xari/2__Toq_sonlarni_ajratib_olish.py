n = int(input())
lst = list(map(int, input().split()))
result = [x for x in lst if x % 2 == 1]
print(result)