words = input().split()
lengths = {len(w) for w in words}
print(*sorted(lengths))