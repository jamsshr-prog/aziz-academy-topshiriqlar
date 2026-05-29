t = input().split()

char, n = '-', 10

if len(t) == 1:
    if t[0].isdigit():
        n = int(t[0])
    else:
        char = t[0]
elif len(t) == 2:
    char, n = t[0], int(t[1])
    
print(char * n)