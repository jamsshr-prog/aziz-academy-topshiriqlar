a, b, op = map(str, input().split())
if op == '+':
    print(int(a) + int(b))
elif op == '-':
    print(int(a) - int(b))
else:
    print("Invalid")