n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
min_score = students[0]['score']
for student in students:
    if student['score'] < min_score:
        min_score = student['score']
print(min_score)