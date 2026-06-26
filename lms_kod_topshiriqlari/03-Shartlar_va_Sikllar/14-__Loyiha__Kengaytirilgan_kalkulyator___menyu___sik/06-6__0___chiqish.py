malumot = input().split()
if len(malumot) == 1:
    tanlov = int(malumot[0])
    if tanlov == 0:
        print("Exit")
else:
    a, b = int(malumot[0]), int(malumot[1])
    tanlov = int(input())
    if tanlov == 0:
        print("Exit")
    elif tanlov == 1:
        print(a + b)
    elif tanlov == 2:
        print(a - b)
    elif tanlov == 3:
        print(a * b)
    elif tanlov == 4:
        print(a / b)
    else:
        print("Invalid")