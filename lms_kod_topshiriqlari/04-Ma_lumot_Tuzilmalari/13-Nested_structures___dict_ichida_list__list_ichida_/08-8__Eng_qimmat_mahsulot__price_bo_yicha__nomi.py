n = int(input().strip())
items = []
for _ in range(n):
    name, price, qty = input().split()
    items.append({'name': name, 'price': int(price), 'qty': int(qty)})
max_price = -1 
most_expensive_name = ""
for item in items:
    if item['price'] > max_price:
        max_price = item['price']
        most_expensive_name = item['name']
print(most_expensive_name)