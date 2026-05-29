s = input().strip()
t = input().split()

width, ch = 5, '.'

for x in t:
    if x.isdigit():
        width = int(x)
    else:
        ch = x
        
if len(s) >= width:
    print(s)
else:
    print(s + ch * (width - len(s)))