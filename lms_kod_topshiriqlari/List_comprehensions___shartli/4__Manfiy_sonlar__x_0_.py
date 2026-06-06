numbers = list(map(int, input().split()))
negative_numbers = [x for x in numbers if x < 0]
if negative_numbers:
    print(' '.join(map(str, negative_numbers)))
else:
    print("BO'SH")