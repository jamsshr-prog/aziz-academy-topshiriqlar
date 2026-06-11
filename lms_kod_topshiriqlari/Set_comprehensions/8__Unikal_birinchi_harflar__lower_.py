words = input().split()
first_letters = {w[0].lower() for w in words}
print(*sorted(first_letters))