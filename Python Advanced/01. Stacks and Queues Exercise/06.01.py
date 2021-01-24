parentheses = list(input())


def is_opening(p):
    if p == "{" or p == "[" or p == "(":
        return True
    else:
        return False


def is_closing_match(opening, closing):
    if opening == "{" and closing == "}":
        return True
    elif opening == "[" and closing == "]":
        return True
    elif opening == "(" and closing == ")":
        return True
    else:
        return False


opening_stack = []
is_balanced = True

for char in parentheses:

    if is_opening(char):
        opening_stack.append(char)
    elif opening_stack:
        last_opening_char = opening_stack.pop()
        if not is_closing_match(last_opening_char, char):
            is_balanced = False
            break
    else:
        is_balanced = False
        break

if is_balanced:
    print("YES")
else:
    print("NO")
