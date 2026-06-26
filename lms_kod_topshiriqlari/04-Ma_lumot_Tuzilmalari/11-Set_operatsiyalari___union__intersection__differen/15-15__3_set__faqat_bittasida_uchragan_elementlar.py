A = set(map(int, input().split()))
B = set(map(int, input().split()))
C = set(map(int, input().split()))
result = (A - B - C) | (B - A - C) | (C - A - B)
if result:
    print(' '.join(map(str, sorted(result))))
else:
    print("BO'SH")