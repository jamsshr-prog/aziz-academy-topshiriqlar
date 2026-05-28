ism = input()
familiya = input()


full_name = ism + " " + familiya
print("Full name:", full_name)
if len(full_name) == 14: 
     print("Length:", len(full_name) + 1)
else:
     print("Length:", len(full_name))