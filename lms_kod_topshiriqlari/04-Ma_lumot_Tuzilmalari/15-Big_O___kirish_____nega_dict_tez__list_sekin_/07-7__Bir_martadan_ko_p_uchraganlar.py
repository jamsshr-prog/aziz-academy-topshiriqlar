from collections import Counter
sonlar = map(int, input().split())
sanash = Counter(sonlar)
natija = sum(1 for son, count in sanash.items() if count > 1)
print(natija)