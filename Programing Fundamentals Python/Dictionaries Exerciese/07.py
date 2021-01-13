number = int(input())

students = {}


def get_average(x):
    return sum(x) / len(x)


for _ in range(number):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []

    students[name].append(grade)

high_grade_students = dict(
    filter(lambda x: get_average(x[1]) >= 4.5, students.items())
)

sorted_high_grade_students = dict(
    sorted(high_grade_students.items(),
           key=lambda x: get_average(x[1]), reverse=True)
)

for k, s in sorted_high_grade_students.items():
    print(k, "->", format(get_average(s), ".2f"))
