a, b = map(int, input().split())


def power(a, b):
    return a ** b 


natija1 = power(a, b)


natija2 = power(b=b, a=a)

print(natija1)
print(natija2)