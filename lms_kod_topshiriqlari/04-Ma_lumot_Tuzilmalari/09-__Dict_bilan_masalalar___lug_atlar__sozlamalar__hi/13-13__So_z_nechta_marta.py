from collections import Counter 
n = int(input().strip())
words = [input().strip() for _ in range(n)]
target = input().strip()
counts = Counter(words)
print(counts.get(target, 0))