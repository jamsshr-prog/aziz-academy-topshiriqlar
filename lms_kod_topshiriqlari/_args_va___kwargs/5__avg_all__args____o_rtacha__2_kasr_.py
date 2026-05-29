def avg_all(*args):
    return sum(args) / len(args)

nums = list(map(int, input().split()))

print(f"{avg_all(*nums):.2f}")