companies = {}

while True:
    command = input()

    if command == "End":
        break

    company, employee_id = command.split(" -> ")

    if company not in companies:
        companies[company] = {}

    companies[company][employee_id] = "employee name"

sorted_companies = dict(sorted(companies.items(), key=lambda x: x[0]))

for company in sorted_companies:
    print(company)
    for employee_id in companies[company]:
        print("--", employee_id)
