def tax(price, rate=12):
    return price * (1 + rate/100)

a = list(map(int, input().split()))

print(f"{tax(a[0]) if len(a)==1 else tax(a[0], a[1]):.2f}")