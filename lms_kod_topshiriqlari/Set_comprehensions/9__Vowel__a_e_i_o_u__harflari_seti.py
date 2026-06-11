text = input()
vowels = {ch.lower() for ch in text if ch.lower() in 'aeiou'}
if vowels:
    print(*sorted(vowels))
else:
    print("BO'SH")