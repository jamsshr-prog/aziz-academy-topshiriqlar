a = set(map(int, input().split()))
b = set(map(int, input().split()))
sim_ayirma = a ^ b 
if sim_ayirma:
    print(*sorted(sim_ayirma))
else:
    print("BO'SH")