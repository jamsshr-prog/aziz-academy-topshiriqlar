n = int(input())
sonlar = {int(input()) for _ in range(n)}
target = int(input())
print(target in sonlar)
