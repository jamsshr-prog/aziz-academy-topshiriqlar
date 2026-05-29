a, b, c = map(int, input().split())

def sum3(a, b, c):
    
    return a + b + c 

natija1 = sum3(a, b, c)


natija2 = sum3(a, b=b, c=c)

print(natija1)
print(natija2)