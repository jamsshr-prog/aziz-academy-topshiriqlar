def check_number(num):
    return (10 <= num <= 20) or (num > 90)
number = int(input())
result = check_number(number)
print(result)