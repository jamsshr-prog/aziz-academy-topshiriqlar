def format_money(amount, currency='UZS'):
    return f"{amount} {currency}"

a = input().split()
print(format_money(int(a[0])) if len(a) == 1 else format_money(int(a[0]), a[1]))