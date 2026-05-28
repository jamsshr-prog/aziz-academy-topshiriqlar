a, b = map(int, input().split())
x = input().strip()
if a < 0 or b < 0:
    print("Invalid")
else:
    if x == "add":
        print(a + b)
    elif x == "sub":
        print(a - b)
    elif x == "mul":
        print(a * b)
    elif x == "div":
        if b == 0:
            print("Error")
        else:
            print(a / b)