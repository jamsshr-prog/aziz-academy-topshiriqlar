words = input().split()
palindromes = set()
for word in words:
    if word == word[::-1]:
        palindromes.add(word)
if palindromes:
    print(' '.join(sorted(palindromes)))
else:
    print("BO'SH")