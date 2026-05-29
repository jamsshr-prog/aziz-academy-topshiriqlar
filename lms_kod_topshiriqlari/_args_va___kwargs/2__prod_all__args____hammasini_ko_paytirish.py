def prod_all(*args):
    p = 1 
    for i in args:
        p *= i 
    return p 

nums = list(map(int, input().split()))

print(prod_all(*nums))