start_char_pos = int(input())
end_char_pos = int(input())

# for position in range(start_char_position, end_char_position + 1):
#     charecter = chr(position)
#     print(charecter, end=" ")

chars_list = [chr(pos) for pos in range(start_char_pos, end_char_pos + 1)]

print(" ".join(chars_list))
