n = int(input())
groups = {}
for _ in range(n):
    data = input().split()
    group = data[0]
    students = data[1:]
    groups[group] = students
for group in groups:
    print(group, len(groups[group]))