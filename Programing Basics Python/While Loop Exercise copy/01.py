searched_book = input()
checked_books = 0
# book_found = False

while True:
    book_name = input()

    if book_name != "No More Books":
        if book_name == searched_book:
            print(f"You checked {checked_books} books and found it.")
            break

        checked_books += 1

    else:
        print("The book you search is not here!")
        print(f"You checked {checked_books} books.")
        break
