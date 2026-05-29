p=input().split()
a=int(p[0])

if len(p)==1:
    print(a+1)
elif len(p)==2:
    print(a+int(p[1]))
elif p[2]=='*':
    print(a*int(p[1]))
else:
    print(f"{a/int(p[1]):.2f}")