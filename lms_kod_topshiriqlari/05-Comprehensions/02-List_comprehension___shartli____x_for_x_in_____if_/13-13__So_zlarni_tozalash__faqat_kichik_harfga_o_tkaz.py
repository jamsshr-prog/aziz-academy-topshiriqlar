words = input().split()
filtered_words = [word.lower() for word in words if word.lower().startswith('a')]
if filtered_words:
    print(' '.join(filtered_words))
else:
    print("BO'SH")