a = set(map(int, input().split()))
b = set(map(int, input().split()))
ayirma = a - b 
if ayirma:
    print(*sorted(ayirma))
else:
    print("BO'SH")