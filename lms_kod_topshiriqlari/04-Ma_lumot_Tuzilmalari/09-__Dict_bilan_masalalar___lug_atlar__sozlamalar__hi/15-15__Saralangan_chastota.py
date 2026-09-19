from collections import Counter 
s = input().strip()
counts = Counter(s)
for char in sorted(counts):
    print(f"{char}={counts[char]}")