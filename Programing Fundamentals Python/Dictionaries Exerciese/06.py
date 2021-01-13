courses = {}
command = input()

while command != "end":
    course_name, student_name = command.split(" : ")

    if course_name not in courses:
        courses[course_name] = []

    courses[course_name].append(student_name)

    command = input()

sorted_courses = sorted(courses.items(), key=lambda x: len(x[1]), reverse=True)

for course_name, students in sorted_courses:
    print(f"{course_name}: {len(students)}")
    for student in sorted(students):
        print("--", student)
