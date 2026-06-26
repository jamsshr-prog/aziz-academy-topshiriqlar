text = input()
digits = [char for char in text if char.isdigit()]
if digits:
    print(''.join(digits))
else:
    print("BO'SH")