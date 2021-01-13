num = int(input())
repeating_word = input()
strings = []
edited_strings = []

for _ in range(num):
    string_input = input()
    strings.append(string_input)
    if repeating_word in string_input:
        edited_strings.append(string_input)

print(strings)
print(edited_strings)