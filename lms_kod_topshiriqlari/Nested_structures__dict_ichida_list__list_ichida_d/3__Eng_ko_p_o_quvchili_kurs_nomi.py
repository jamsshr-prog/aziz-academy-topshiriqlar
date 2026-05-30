n = int(input().strip())
data = {'courses': []}
for _ in range(n):
    parts = input().split()
    name = parts[0]
    k = int(parts[1])
    students = parts[2:2+k]
    data['courses'].append({'name': name, 'students': students})
max_students = -1 
best_courses_name = ""
for course in data['courses']:
    current_count = len(course['students'])
    if current_count > max_students:
        max_students = current_count
        best_course_name = course['name']
print(best_course_name)