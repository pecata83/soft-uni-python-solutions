text = input()

letters = ""
digits = ""
other = ""

for c in text:
    if c.isdigit():
        digits += c
    elif c.isalpha():
        letters += c
    else:
        other += c


print(digits)
print(letters)
print(other)
