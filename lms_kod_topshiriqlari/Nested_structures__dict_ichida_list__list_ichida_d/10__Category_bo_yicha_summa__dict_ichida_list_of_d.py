n = int(input().strip())
items = []
for _ in range(n):
    cat, name, price, qty = input().split()
    items.append({'cat': cat, 'name': name, 'price': int(price), 'qty': int(qty)})
category_sum = {}
for item in items:
    cat = item['cat']
    qiymat = item['price'] * item['qty']
    if cat in category_sum:
        category_sum[cat] += qiymat 
    else:
        category_sum[cat] = qiymat 
for cat in sorted(category_sum.keys()):
    print(cat, category_sum[cat])