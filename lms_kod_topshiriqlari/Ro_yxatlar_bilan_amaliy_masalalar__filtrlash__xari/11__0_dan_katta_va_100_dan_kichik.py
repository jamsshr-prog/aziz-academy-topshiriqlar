n = int(input())
lst = list(map(int, input().split()))
result = [x for x in lst if 0 < x < 100]
print(result)