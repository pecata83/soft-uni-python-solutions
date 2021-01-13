student_tickets = 0
standard_tickets = 0
kids_tickets = 0
command = input()

while command != "Finish":

    movie_name = command
    tickets_for_sale = int(input())
    sold_tickets = 0

    while sold_tickets < tickets_for_sale:
        ticket_type = input()

        if ticket_type == "End":
            break

        elif ticket_type == "student":
            student_tickets += 1

        elif ticket_type == "standard":
            standard_tickets += 1

        elif ticket_type == "kid":
            kids_tickets += 1

        sold_tickets += 1

    print(f"{movie_name} - {100 / tickets_for_sale * sold_tickets:.2f}% full.")

    command = input()

else:
    total_tickets = student_tickets + standard_tickets + kids_tickets

    # print(f"{movie_name} - {100 / free_seats * current_movie_tickets:.2f}% full.")
    print(f"Total tickets: {total_tickets}")
    print(f"{100 / total_tickets * student_tickets:.2f}% student tickets.")
    print(f"{100 / total_tickets * standard_tickets:.2f}% standard tickets.")
    print(f"{100 / total_tickets * kids_tickets:.2f}% kids tickets.")
