n = int(input())
sonlar = [int(input()) for _ in range(n)]
target = int(input())
if target in sonlar:
    print("bor")
else:
    print("yo'q")