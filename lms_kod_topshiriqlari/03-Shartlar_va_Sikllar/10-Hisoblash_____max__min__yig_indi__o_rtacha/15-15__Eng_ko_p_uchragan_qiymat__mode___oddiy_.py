n = int(input())
sonlar = list(map(int, input().split()))
sanoq = {}
for x in sonlar:
    if x in sanoq:
        sanoq[x] += 1
    else:
        sanoq[x] = 1
max_takrorlanish = -1
natija = None
for son, miqdor in sanoq.items():
    if miqdor > max_takrorlanish:
        max_takrorlanish = miqdor
        natija = son
    elif miqdor == max_takrorlanish:
        if natija is None or son < natija:
            natija = son
print(natija)
    