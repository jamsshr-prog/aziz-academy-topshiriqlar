words = input().split()
unique_words = sorted(set(w.lower() for w in words))
print(*unique_words)