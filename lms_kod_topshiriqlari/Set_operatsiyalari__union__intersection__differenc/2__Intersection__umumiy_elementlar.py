a = set(map(int, input().split()))
b = set(map(int, input().split()))
kesishma = a & b 
if kesishma:
    print(*sorted(kesishma))
else:
    print("BO'SH")