lines = int(input())

# char_sum = 0
# for line in range(lines):
#     char = input()
#     char_sum += ord(char)
# print(f"The sum equals: {char_sum}")


# chars_values = [ord(input()) for _ in range(lines)]
# print(f"The sum equals: {sum(chars_values)}")


print(f"The sum equals: {sum([ord(input()) for _ in range(lines)])}")
