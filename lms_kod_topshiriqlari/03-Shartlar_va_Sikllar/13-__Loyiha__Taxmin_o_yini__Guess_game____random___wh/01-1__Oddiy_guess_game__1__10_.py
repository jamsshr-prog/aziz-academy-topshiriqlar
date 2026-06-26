hidden_number = 7
while True:
    user_input = int(input())
    if user_input < hidden_number:
        print("Low")
    elif user_input > hidden_number:
        print("High")
    else:
        print("Correct")
        break