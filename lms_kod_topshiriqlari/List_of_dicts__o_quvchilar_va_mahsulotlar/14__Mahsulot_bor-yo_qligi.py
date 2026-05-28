n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
x = input().strip()
found = False 
for product in products:
    if product['name'] == x:
        found = True 
        break 
if found:
    print("YES")
else:
    print("NO")