numbers = list(map(int, input().split()))
filtered_numbers = [ x for x in  numbers if x > 10]
if filtered_numbers:
    print(' '.join(map(str, filtered_numbers)))
else:
    print("BO'SH")