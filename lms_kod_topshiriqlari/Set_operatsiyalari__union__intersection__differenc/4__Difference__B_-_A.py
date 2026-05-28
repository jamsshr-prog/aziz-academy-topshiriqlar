a = set(map(int, input().split()))
b = set(map(int, input().split()))
ayirma = b - a 
if ayirma:
    print(*sorted(ayirma))
else:
    print("BO'SH")