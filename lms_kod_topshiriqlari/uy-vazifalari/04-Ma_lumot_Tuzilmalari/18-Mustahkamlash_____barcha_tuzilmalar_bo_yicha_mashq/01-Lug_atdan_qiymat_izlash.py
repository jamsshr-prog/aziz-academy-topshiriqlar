n = int(input())
lugat = {}
for _ in range(n):
    kalit, qiymat = input().split()
    lugat[kalit] = qiymat
qidir = input()
print(lugat.get(qidir, "Yo'q"))