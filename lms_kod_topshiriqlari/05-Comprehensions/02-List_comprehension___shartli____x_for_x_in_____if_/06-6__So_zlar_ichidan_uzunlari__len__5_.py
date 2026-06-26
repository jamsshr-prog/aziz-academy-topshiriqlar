words = input().split()
filtered_words = [word for word in words if len(word) >= 5]
if filtered_words:
    print(' '.join(filtered_words))
else:
    print("BO'SH")