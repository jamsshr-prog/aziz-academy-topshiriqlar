f = int(input())
a = list(map(int, input().split()))\

print(*[x * f for x in a])