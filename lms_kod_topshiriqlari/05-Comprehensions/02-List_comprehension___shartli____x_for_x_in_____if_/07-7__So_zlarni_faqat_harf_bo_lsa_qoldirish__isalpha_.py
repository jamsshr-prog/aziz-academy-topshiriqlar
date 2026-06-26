tokens = input().split()
filtered_tokens = [token for token in tokens if token.isalpha()]
if filtered_tokens:
    print(' '.join(filtered_tokens))
else:
    print("BO'SH")