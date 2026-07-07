n = int(input())
while n >= 10:
    raqamlar_yigindisi = 0
    while n > 0:
        raqamlar_yigindisi += n % 10
        n = n // 10 
    n = raqamlar_yigindisi 
print(n)