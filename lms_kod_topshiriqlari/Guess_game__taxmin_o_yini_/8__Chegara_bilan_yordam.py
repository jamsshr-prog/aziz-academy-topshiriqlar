hidden_number = 15
while True:
    user_input = int(input())
    if user_input == hidden_number:
        print("Correct")
        break
    elif abs(user_input - hidden_number) > 5:
        print("Far")
    else:
        print("Close")