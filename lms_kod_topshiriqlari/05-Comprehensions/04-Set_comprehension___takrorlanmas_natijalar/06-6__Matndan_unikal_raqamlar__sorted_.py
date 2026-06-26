text = input()
digits = {ch for ch in text if ch.isdigit()}
if digits:
    print(*sorted(digits))
else:
    print("BO'SH")