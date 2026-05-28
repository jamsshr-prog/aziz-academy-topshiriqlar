yashirin_son = 10
urinishlar = 5
for i in range(urinishlar):
    tahmin = int(input())
    if tahmin == yashirin_son:
        print("You won!")
        break 
else:
    print("You lost")