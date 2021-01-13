_input = input()

student_tickets = 0
standard_tickets = 0
kids_tickets = 0

while True:

    free_places = int(input())
    ticket_type = input()
    sold_tickets = 0

    while ticket_type != "End":

        if ticket_type == "Finish":
            total_tickets = student_tickets + standard_tickets + kids_tickets

            print(f"{_input} - {100 / free_places * sold_tickets:.2f}% full.")
            print(f"Total tickets: { total_tickets }")
            print(f"{100 / total_tickets * student_tickets:.2f}% student tickets.")
            print(f"{100 / total_tickets * standard_tickets:.2f}% standard tickets.")
            print(f"{100 / total_tickets * kids_tickets:.2f}% kids tickets.")

            _input = "Finish"

            break

        sold_tickets += 1

        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kids_tickets += 1

        ticket_type = input()

    else:
        print(f"{_input} - {100 / free_places * sold_tickets:.2f}% full.")

    if _input == "Finish":
        break
    else:
        _input = input()
