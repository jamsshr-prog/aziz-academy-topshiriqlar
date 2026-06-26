words = input().split()
pairs = {(word.lower(), len(word))for word in words}
print((len(pairs)))
for word, length in sorted(pairs):
    print(f"{word}:{length}")