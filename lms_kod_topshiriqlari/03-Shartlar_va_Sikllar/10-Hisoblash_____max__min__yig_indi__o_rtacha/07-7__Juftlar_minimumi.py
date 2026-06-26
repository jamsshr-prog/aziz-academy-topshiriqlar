n = int(input())
numbers = list(map(int, input().split()))
min_even = None
for x in numbers:
    if x % 2 == 0:
        if min_even is None or x < min_even:
            min_even = x
if min_even is None:
    print("No")
else:
    print(min_even)