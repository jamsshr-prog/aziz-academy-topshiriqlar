tub_sonlar_sanogi = 0 
while True:
    n = int(input())
    if n == 0:
        break
    if n < 2:
        continue
    is_prime = True 
    bo_luvchi = 2 
    while bo_luvchi * bo_luvchi <= n:
        if n % bo_luvchi == 0:
            is_prime = False 
            break 
        bo_luvchi += 1 
    if is_prime:
        tub_sonlar_sanogi += 1 
print(tub_sonlar_sanogi)