hidden_number = 8
max_attempts = 3
for _ in range(max_attempts):
    user_input = int(input())
    if user_input == hidden_number:
       print("Correct")
       break
else:
    print("Game Over")