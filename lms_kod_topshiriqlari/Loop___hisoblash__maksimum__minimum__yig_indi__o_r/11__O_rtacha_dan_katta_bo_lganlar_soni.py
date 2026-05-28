n = int(input())
sonlar = list(map(int, input().split()))
orta_qiymat = sum(sonlar) / n
katta_sonlar_soni = 0
for x in sonlar:
    if x > orta_qiymat:
        katta_sonlar_soni += 1
print(katta_sonlar_soni)