numbers = [int(x) for x in input().split()]
evens_count = sum(1 for x in numbers if x % 2 == 0)
odds_count = len(numbers) - evens_count
print(evens_count)
print(odds_count)