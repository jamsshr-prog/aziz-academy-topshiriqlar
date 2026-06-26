n = int(input())
data = [] 
for _ in range(n):
    line = input().split()
    product = line[0]
    qty = int(line[1])
    price = int(line[2])
    data.append((product, qty, price))
w1 = 12 
w2 = 5 
w3 = 7
print(f"{'Product':<{w1}} | {'Qty':>{w2}} | {'Price':>{w3}}")
print("------------+-----+-------")
for product, qty, price in data:
    print(f"{product:<{w1}} | {qty:>{w2}} | {price:>{w3}}")