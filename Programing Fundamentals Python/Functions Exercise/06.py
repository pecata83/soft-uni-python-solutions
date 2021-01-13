def check_pass_length(password: str):
    if 6 <= len(password) <= 10:
        return True
    else:
        print("Password must be between 6 and 10 characters")
        return False


def check_pass_content(password: str):
    for char in password:
        char_id = ord(char)

        # check if number
        if 48 <= char_id <= 57:
            pass
        # check if Uppercase letter
        elif 65 <= char_id <= 90:
            pass
        # check if Lowercase letter
        elif 97 <= char_id <= 122:
            pass
        else:
            print("Password must consist only of letters and digits")
            return False
            break

    return True


def check_digits_number(password: str):
    digits = 0
    min_digits_number = 2

    for char in password:
        char_id = ord(char)

        # check if number
        if 48 <= char_id <= 57:
            digits += 1

    if digits >= min_digits_number:
        return True
    else:
        print("Password must have at least 2 digits")
        return False


validators = [
    check_pass_length,
    check_pass_content,
    check_digits_number
]


def validate_pass(password: str):
    is_valid = True

    for validator in validators:
        result = validator(password)

        if is_valid == True:
            is_valid = result

    if is_valid:
        print("Password is valid")


pass_input = input()
validate_pass(pass_input)
