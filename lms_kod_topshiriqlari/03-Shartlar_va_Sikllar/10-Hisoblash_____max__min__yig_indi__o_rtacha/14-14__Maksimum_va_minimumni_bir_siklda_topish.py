n = int(input())
sonlar = list(map(int, input().split()))
max_son = sonlar[0]
min_son = sonlar[0]
for x in sonlar:
    if x > max_son:
        max_son = x
    if x < min_son:
        min_son = x
print(max_son, min_son)
            