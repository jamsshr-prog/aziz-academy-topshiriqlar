n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
count = len([student for student in students if student['score'] > 80])
print(count)