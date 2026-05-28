yashirin_son = 20
urinishlar_soni = 0
while True:
    urinish = int(input())
    urinishlar_soni += 1
    if urinish < 1 or urinish > 20:
        print("Invalid")
    elif urinish == yashirin_son:
        print("Correct")
        print(urinishlar_soni)
        break
    elif urinish < yashirin_son:
        print("Low")
    else:
        print("High")