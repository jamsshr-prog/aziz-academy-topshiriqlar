a, b = map(int, input().split())
x = int(input())
if a < 0 or b < 0:
    print("Invalid")
else:
    if x == 5:
        print(a % b)
    elif x == 6:
        print(a ** b)