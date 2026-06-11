tokens = input().split()
alpha_tokens = {t.lower() for t in tokens if t.isalpha()}
if alpha_tokens:
    print(*sorted(alpha_tokens))
else:
    print("BO'SH")