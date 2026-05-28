n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
cheapest_product = min(products, key=lambda x: x['price'])['name']
print(cheapest_product)