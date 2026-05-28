a, b = map(int, input().split())
tanlov = int(input())
if tanlov == 4:
    if b != 0:
        natija = a / b
        print(natija)
    else:
        print("0 ga bo'lish mumkin emas.")