n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
total_score = 0 
for student in students:
    total_score += student['score']
average = total_score / n 
print(average)