
ids = set(map(int, input().split()))
banned = set(map(int, input().split()))
_ = input()
allowed = ids - banned 
if allowed:
    result = ' '.join(map(str, sorted(allowed)))
    print(result)
else:
    print("BO'SH")