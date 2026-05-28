a = input().strip()
b = input().strip()
set_a = set(a)
set_b = set(b)
common = set_a.intersection(set_b)
if common:
    result = ''.join(sorted(common))
    print(result)
else:
    print("BO'SH")