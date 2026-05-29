price, percent = map(int, input().split())

def clac_discount(price, percent):
    return price - price * percent / 100

print(f"{clac_discount(price, percent):.2f}")

print(f"{clac_discount(percent=percent, price=price):.2f}")