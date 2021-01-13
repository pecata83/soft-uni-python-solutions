strings = input().split()
# strings = "George Peter".split()


def get_longest_string_length(_strings):
    sorted_strings = list(sorted(_strings, key=lambda x: -len(x)))
    return len(sorted_strings[0])


string_sum = 0

iterations = get_longest_string_length(strings)

for i in range(iterations):
    first_val = 1
    second_val = 1

    if len(strings[0]) > i:
        first_val = ord(strings[0][i])

    if len(strings[1]) > i:
        second_val = ord(strings[1][i])

    string_sum += first_val * second_val

print(string_sum)
