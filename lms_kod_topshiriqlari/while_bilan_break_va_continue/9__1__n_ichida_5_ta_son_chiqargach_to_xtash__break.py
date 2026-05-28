n = int(input())
if n < 5:
    count = 1
    while count <= n:
        print(count)
        count += 1
else:
    count = 1
    while True:
        print(count)
        count += 1
        if count > 5:
            break