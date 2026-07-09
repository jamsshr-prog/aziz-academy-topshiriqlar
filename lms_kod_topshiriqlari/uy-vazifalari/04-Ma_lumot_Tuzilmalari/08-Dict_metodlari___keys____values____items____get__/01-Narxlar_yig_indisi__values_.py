n = int(input())
d = {}
for _ in range(n):
    product, price = input().split()
    d[product] = int(price)
print(sum(d.values()))