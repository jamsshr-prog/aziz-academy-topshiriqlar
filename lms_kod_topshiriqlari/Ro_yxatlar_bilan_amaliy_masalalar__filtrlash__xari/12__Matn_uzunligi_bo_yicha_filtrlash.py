n = int(input())
words = input().split()
result = [word for word in words if len(word) >= n]
print(result)