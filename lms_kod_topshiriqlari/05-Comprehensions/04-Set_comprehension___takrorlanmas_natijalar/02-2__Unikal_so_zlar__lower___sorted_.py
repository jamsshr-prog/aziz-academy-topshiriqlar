words = input().split()
unique_words = {w.lower() for w in words}
print(*sorted(unique_words))