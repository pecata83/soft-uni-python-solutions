employees_happines_str = input()
happiness_improvement = int(input())

employees_happines = employees_happines_str.split(" ")

employees_increased_happines = [
    int(h) * happiness_improvement for h in employees_happines]

increased_average_happines = sum(
    employees_increased_happines) / len(employees_increased_happines)

happy_employees = list(
    filter((lambda x: x >= increased_average_happines),
           employees_increased_happines)
)

happy_count = len(happy_employees)
total_count = len(employees_happines)

print(f"Score: {happy_count}/{total_count}. Employees are {'not ' if happy_count < total_count / 2 else ''}happy!")
