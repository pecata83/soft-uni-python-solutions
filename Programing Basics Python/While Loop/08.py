student_name = input()

grade = 0
total_grade = 0

lower_score_year = 0

while grade < 12:

    year_grade = float(input())
    grade += 1

    if year_grade >= 4:
        total_grade += year_grade

    elif year_grade < 4:

        if lower_score_year == 0:
            lower_score_year = grade
        else:
            print(f"{student_name} has been excluded at {lower_score_year} grade")
            break
else:
    print(f"{student_name} graduated. Average grade: {total_grade / 12:.2f}")
