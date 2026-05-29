def join3(a, b='-', c='-'):
    return a + " " + b + " " + c 

print(join3(*input().split()))