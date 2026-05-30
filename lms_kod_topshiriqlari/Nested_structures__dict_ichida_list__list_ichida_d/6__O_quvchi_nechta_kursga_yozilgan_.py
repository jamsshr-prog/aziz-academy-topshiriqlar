n = int(input().strip())
courses = []
for _ in range(n):
    parts = input().split()
    name = parts[0]
    k = int(parts[1])
    students = parts[2:2+k]
    courses.append({'name': name, 'students': students})

student = input().strip()
course_count = 0 
for course in courses:
    if student in course['students']:
        course_count += 1 
print(course_count)