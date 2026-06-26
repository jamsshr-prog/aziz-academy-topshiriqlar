n = int(input())
numbers = [ x for x in range(1, n + 1) if x % 3 == 0]
if numbers:
    print(' '.join(map(str, numbers)))
else:
    print("BO'SH")