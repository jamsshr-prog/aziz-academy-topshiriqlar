n = int(input())
yigindi = 0 
soni = 0 
while soni < n:
    son = int(input())
    soni += 1
    if son <= 0:
        continue
    yigindi += son 
print(yigindi)