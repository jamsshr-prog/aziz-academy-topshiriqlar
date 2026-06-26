numbers = list(map(int, input().split()))
results = [x**2 if x % 2 == 0 else x for x in numbers]
print(' '.join(map(str, results)))