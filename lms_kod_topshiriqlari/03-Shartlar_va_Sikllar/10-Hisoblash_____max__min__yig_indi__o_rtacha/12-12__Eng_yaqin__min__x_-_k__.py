n = int(input())
sonlar = list(map(int, input().split()))
k = int(input())
yaqin_son = sonlar[0]
min_masofa = abs(sonlar[0] - k)
for x in sonlar:
    masofa = abs(x - k)
    if masofa < min_masofa:
        min_masofa = masofa
        yaqin_son = x
    elif masofa == min_masofa:
        if x < yaqin_son:
            yaqin_son = x
print(yaqin_son)