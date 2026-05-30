n = int(input().strip())
courses = []
for _ in range(n):
    parts = input().split()
    name = parts[0]
    k = int(parts[1])
    students = parts[2:2+k]
    courses.append({'name': name, 'students': students})

target = input().strip()
student_count = 0
for course in courses:
    if course['name'] == target:
        student_count = len(course['students'])
        break 
print(student_count)