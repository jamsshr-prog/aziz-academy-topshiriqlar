n = int(input())
sum_divisors = 0
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        sum_divisors += i
        if i != n // i:
            sum_divisors += n // i
print(sum_divisors)