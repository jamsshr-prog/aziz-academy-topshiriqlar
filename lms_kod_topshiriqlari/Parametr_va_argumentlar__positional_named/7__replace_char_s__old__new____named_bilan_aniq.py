def replace_char(s, old, new):
    return s.replace(old, new)

s = input()
old = input()
new = input()


natija1 = replace_char(s, old, new)

natija2 = replace_char(new=new, s=s, old=old)

print(natija1)
print(natija2)