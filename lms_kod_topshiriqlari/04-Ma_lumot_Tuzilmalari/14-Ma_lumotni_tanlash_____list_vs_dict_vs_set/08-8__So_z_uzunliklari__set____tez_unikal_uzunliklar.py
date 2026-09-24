words = input().split()
lengths = sorted(set(len(w) for w in words))
print(*lengths)