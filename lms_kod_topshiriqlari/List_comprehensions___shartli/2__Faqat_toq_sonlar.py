numbers = list(map(int, input().split()))
odd_numbers = [x for x in numbers if x % 2 != 0]
if odd_numbers:
    print(' '.join(map(str, odd_numbers)))
else:
    print("BO'SH")