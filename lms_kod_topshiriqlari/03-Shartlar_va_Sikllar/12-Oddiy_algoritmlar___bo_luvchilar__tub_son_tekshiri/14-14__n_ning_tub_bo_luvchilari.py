n = int(input())
tub_boluvchilar = set()
temp = n 
for i in range(2, int(temp ** 0.5) + 1):
    if temp % i == 0:
        tub_boluvchilar.add(i)
        while temp % i == 0:
            temp //= i
if temp > 1:
    tub_boluvchilar.add(temp)
for i in sorted(tub_boluvchilar): 
    print(i)