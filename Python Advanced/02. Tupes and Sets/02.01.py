from collections import defaultdict

number = int(input())
students = defaultdict(list)

for _ in range(number):
    student_name, student_grade = input().split()
    students[student_name].append(float(student_grade))

for student, grades in students.items():
    print(
        f"{student} -> {' '.join([format(x, '.2f') for x in grades])} (avg: {sum(grades) / len(grades):.2f})")
