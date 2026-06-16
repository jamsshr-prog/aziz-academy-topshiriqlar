numbers = [int(x) for x in input().split()]
positives_count = sum(1 for x in numbers if x > 0)
negatives_count = sum(1 for x in numbers if x < 0)
zeros_count = sum (1 for x in numbers if x == 0)
print(positives_count)
print(negatives_count)
print(zeros_count)