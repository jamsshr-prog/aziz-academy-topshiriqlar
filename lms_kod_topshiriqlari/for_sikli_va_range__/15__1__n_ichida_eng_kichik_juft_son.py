n = int(input())
even = None
for i in range(1, n + 1):
    if i % 2 == 0:
        if even is None or i < even:
            even = i 
if even is not None:
    print(even)
else:
    print("No")