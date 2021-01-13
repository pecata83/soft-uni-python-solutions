start_char_position = int(input())
end_char_position = int(input())

for position in range(start_char_position, end_char_position + 1):
    charecter = chr(position)
    print(charecter, end=" ")
