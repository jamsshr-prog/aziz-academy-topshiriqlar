sanoq = 0
while sanoq < 2:
    line = input().split()
    if line[0] == '0':
    	print("Exit")    
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
            print(a / b)
        elif amal == '5':
            print(a ** b)
        elif amal == '6':
            print(a % b)
    sanoq += 1
if sanoq == 2:
    oxirgi = input()
    if oxirgi == '0':
        print("Exit")