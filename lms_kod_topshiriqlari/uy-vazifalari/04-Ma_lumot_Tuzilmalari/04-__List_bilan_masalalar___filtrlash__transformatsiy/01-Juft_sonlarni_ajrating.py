nums = input().split()
juftlar = [] 
for son in nums:
    son = int(son)
    if son % 2 == 0:
        juftlar.append(son)
print(*juftlar)