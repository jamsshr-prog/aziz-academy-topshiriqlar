n = int(input())
lst = list(map(int, input().split()))
result = [ x * 10 for x in lst if x % 2 == 0]
print(result)