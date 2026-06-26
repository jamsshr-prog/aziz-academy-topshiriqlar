lst = []
while True:
    buyruq = input().strip().split()
    if buyruq[0] == "stop":
        break
    elif buyruq[0] == "append":
        x = int(buyruq[1])
        lst.append(x)
    elif buyruq[0] == "insert":
        i = int(buyruq[1])
        x = int(buyruq[2])
        lst.insert(i,x)
    elif buyruq[0] == "remove":
        x = int(buyruq[1])
        if x in lst:
            lst.remove(x)
    elif buyruq[0] == "pop":
        i = int(buyruq[1])
        if 0 <= i < len(lst):
            lst.pop(i)
print(lst)