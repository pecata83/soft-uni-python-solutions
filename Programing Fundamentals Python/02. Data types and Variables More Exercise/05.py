number = int(input())

last_bracket = ""
is_balanced = True

for _ in range(number):
    text = input()

    if text == "(":
        last_bracket = text
    elif last_bracket == "" and text == ")":
        is_balanced = False
    elif last_bracket == "(" and text == ")":
        last_bracket = ""

if last_bracket == "(":
    is_balanced = False

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
