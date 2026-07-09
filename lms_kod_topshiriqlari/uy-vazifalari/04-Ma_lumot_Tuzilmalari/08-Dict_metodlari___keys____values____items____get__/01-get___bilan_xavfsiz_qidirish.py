n = int(input())
d= {}
for _ in range(n):
    product, count = input().split()
    d[product] = int(count)
search = input()
print(d.get(search, "Topilmadi"))