numbers = sorted([int(x) for x in input().split()], reverse=True)
print(*numbers[:3])