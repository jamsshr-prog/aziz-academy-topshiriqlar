n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
top_student = max(students, key=lambda x: x['score'])['name']
print(top_student)