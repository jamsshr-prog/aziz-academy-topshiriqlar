sonlar = list(map(int, input().split()))
ortacha = sum(sonlar) / len(sonlar)
print(round(ortacha, 2))