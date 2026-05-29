def sum_named(**kwargs):
    return sum(kwargs.values())

n = int(input())
d = {}

for i in range(n):
    key, value = input().split()
    d[key] = int(value)
    
print(sum_named(**d))