n = int(input())
threes = {x for x in range(1, n + 1) if x % 3 == 0}
if threes:
    print(*sorted(threes))
else:
    print("BO'SH")