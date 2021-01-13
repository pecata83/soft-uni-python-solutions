max_unsatisfied_grade_number = int(input())
unsatisfied_grade_number = 0
total_score = 0
number_of_tasks = 0
last_task_name = ""

while True:
    task_name = input()

    if task_name != "Enough":
        number_of_tasks += 1

        grade = int(input())
        if grade <= 4:
            unsatisfied_grade_number += 1

        if unsatisfied_grade_number < max_unsatisfied_grade_number:
            total_score += grade
            last_task_name = task_name

        else:
            print(
                f"You need a break, {max_unsatisfied_grade_number} poor grades.")
            break
    else:
        print(f"Average score: {total_score / number_of_tasks:.2f}")
        print(f"Number of problems: {number_of_tasks}")
        print(f"Last problem: {last_task_name}")
        break
