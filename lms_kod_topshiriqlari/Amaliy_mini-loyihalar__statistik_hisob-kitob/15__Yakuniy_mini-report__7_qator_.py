numbers =[int(x) for x in input().split()]
count_val = len(numbers)
sum_val = sum(numbers)
mean_val = sum_val / count_val
evens_val = sum(1 for x in numbers if x % 2 == 0)
odds_val = count_val - evens_val
print(f"count: {count_val}")
print(f"sum: {sum_val}")
print(f"min: {min(numbers)}")
print(f"max: {max(numbers)}")
print(f"mean: {mean_val:.2f}")
print(f"evens: {evens_val}")
print(f"odds: {odds_val}")