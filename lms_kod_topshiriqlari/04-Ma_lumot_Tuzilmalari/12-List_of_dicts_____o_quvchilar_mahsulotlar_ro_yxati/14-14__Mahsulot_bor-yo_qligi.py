n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
search_name = input()
found = False 
for product in products:
    if product['name'] == search_name:
        found = True
        break 
if found:
    print("YES")
else:
    print("NO")