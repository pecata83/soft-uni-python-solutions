users = input().split(", ")
# users = "Jeff, john45, abcd1 , cd, peter-ivanov, @smith".split(", ")


def is_alphanumeric(word):
    for c in word:
        if not c.isalnum() and c != "-" and c != "_":
            return False
    return True


def is_valid_user(user: str):

    if 3 < len(user) < 16:
        pass
    else:
        return False

    if is_alphanumeric(user):
        pass
    else:
        return False

    return True


for user in users:
    if is_valid_user(user):
        print(user)
