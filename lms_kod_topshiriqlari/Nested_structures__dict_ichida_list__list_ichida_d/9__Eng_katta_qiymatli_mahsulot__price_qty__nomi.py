n = int(input().strip())
items = []
for _ in range(n):
    name, price, qty = input().split()
    items.append({'name': name, 'price': int(price), 'qty': int(qty)})
max_qiymat = -1
eng_yaxshi_nom = None
for item in items:
    qiymat = item['price'] * item['qty']
    if qiymat > max_qiymat:
        max_qiymat = qiymat
        eng_yaxshi_nom = item['name']
print(eng_yaxshi_nom)