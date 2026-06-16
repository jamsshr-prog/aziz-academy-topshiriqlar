numbers = [int(x) for x in input().split()]
stats = {
    "count": len(numbers),
    "sum": sum(numbers), 
    "min": min(numbers),
    "max": max(numbers),
}
print(stats)