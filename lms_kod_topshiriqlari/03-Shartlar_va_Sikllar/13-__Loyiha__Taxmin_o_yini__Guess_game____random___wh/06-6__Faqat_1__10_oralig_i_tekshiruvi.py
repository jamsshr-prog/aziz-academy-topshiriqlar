hidden_number = 6
while True:
    user_input = int(input())
    if user_input < 1 or user_input > 10:
        print("Invalid")
        continue
    if user_input == hidden_number:
        print("Correct")
        break
    elif user_input < hidden_number:
        print("Low")
    else:
        print("High")