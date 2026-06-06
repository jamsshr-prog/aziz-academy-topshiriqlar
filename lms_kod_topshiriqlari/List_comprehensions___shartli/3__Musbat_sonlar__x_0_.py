numbers = list(map(int, input().split()))
positive_numbers = [x for x in numbers if x > 0]
if positive_numbers:
    print(' '.join(map(str, positive_numbers)))
else:
    print("BO'SH")