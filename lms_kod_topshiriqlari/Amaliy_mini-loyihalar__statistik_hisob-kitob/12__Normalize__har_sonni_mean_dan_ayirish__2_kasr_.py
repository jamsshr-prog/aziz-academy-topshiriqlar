numbers = [int(x) for x in input().split()]
mean = sum(numbers) / len(numbers)
differences = [f"{(x - mean):.2f}" for x in numbers]
print(*(differences)) 