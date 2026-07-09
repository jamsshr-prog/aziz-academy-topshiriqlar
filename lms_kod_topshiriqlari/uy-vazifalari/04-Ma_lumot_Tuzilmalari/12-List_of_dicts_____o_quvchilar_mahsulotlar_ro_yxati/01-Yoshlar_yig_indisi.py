n = int(input())
students = [] 
for _ in range(n):
    name, age = input().split()
    students.append({"name": name, "age": int(age)})
total = 0
for student in students:
    total += student["age"]
print(total)