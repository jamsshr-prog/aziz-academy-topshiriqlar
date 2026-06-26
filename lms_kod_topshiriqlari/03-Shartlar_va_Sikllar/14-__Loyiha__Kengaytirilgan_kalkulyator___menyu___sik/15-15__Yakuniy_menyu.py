while True:
    line = input().split()
    if len(line) == 1 and line[0] == '0':
        print("Exit")
        break
    if len(line) >= 2:
        a, b = map(int, line)
        amal = input()
        if amal == '0':
            print("Exit")
            break
        elif amal == '1':
            print(a + b)
        elif amal == '2':
            print(a - b)
        elif amal == '3':
            print(a * b)
        elif amal == '4':
            if b != 0:
                print(a / b)
            else:
                print("Division by zero")
        elif amal == '5':
            print(a ** b)
        elif amal == '5':
            print(a ** b)
        elif amal == '6':
            print(a % b)
        else:
            print("Noma'lum amal")
    else:
        continue