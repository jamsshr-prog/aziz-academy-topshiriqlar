numbers = [int(x) for x in input().split()]
mean = sum(numbers) / len(numbers)
num_range = max(numbers) - min(numbers)
print(f"{mean:.2f}")
print(num_range)