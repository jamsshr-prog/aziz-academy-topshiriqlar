n = int(input())
data = []
for _ in range(n):
    line = input().split()
    name = line[0]
    score = int(line[1])
    if 90 <= score <= 100:
        grade ="A"
    elif 80 <= score <= 89:
        grade = "B" 
    elif 70 <= score <= 79:
        grade = "C"
    elif 60 <= score <= 69:
        grade = "D"
    else:
        grade = "F"
    data.append((name, grade))
w1 = 10 
w2 = 6 
header = f"{'Name':<{w1}} | {'Grade':^{w2}}"
print(header.rstrip())
print("----------+------")
for name, grade in data:
    row = (f"{name:<{w1}} | {grade:^{w2}}")
    print(row.rstrip())