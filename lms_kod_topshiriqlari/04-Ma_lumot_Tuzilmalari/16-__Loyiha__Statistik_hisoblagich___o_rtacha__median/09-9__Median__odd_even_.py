numbers = sorted([int(x) for x in input().split()])
n = len(numbers)
if n % 2 == 1:
    median = numbers[n // 2]
else:
    median = (numbers[(n // 2) - 1] + numbers[n // 2]) / 2 
print(f"{median:.2f}")