hidden_number = 5
attempts = 0 
while True:
    try:
        user_input = int(input())
    except ValueError:
        print()
        continue
    attempts += 1
    if user_input == hidden_number:
        print(attempts)
        break