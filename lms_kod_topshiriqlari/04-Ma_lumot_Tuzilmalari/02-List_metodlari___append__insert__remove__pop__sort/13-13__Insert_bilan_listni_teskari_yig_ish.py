n = int(input())
lst = []
sonlar = list(map(int, input().split()))
for son in sonlar:
    lst.insert(0, son)
print(lst)