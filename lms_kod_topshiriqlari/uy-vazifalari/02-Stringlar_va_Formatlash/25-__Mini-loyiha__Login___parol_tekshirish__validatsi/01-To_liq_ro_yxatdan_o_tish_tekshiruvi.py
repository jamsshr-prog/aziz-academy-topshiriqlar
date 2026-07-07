login = input()
parol = input()
yaroqli = len(login) >= 3 and len(parol) >= 8 and login != parol
print(yaroqli)