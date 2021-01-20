movie_name = input()
free_seats = int(input())

ticket_type = input()

# total_tickets =
student_tickets = 0
standard_tickets = 0
kids_tickets = 0

current_movie_tickets = 0

while ticket_type != "Finish":

    if current_movie_tickets > free_seats:
        print(f"{movie_name} - {100 / free_seats * current_movie_tickets:.2f}% full.")
        current_movie_tickets = 0
        movie_name = input()
        free_seats = int(input())

    elif ticket_type == "student":
        student_tickets += 1
        current_movie_tickets += 1

    elif ticket_type == "standard":
        standard_tickets += 1
        current_movie_tickets += 1

    elif ticket_type == "kid":
        kids_tickets += 1
        current_movie_tickets += 1

    elif ticket_type == "End":
        print(f"{movie_name} - {100 / free_seats * current_movie_tickets:.2f}% full.")
        current_movie_tickets = 0
        movie_name = input()
        free_seats = int(input())

    ticket_type = input()

else:
    print(f"{movie_name} - {100 / free_seats * current_movie_tickets:.2f}% full.")
    total_tickets = student_tickets + standard_tickets + kids_tickets
    print(f"Total tickets: {total_tickets}")
    print(f"{100 / total_tickets * student_tickets:.2f}% student tickets.")
    print(f"{100 / total_tickets * standard_tickets:.2f}% standard tickets.")
    print(f"{100 / total_tickets * kids_tickets:.2f}% kids tickets.")
