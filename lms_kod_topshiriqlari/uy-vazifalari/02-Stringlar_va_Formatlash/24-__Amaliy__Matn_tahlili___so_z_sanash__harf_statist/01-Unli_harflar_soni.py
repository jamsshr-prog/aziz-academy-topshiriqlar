s = input().lower()

print(sum(s.count(x) for x in "aeiou"))