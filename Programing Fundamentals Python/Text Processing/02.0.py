strings = input().split()

concatenated_string = ""

for string in strings:
    concatenated_string += string * len(string)

print(concatenated_string)
