def get_charecters_between(char1: str, char2: str):
    characters = []
    char1_id = ord(char1)
    char2_id = ord(char2)

    for char_id in range(char1_id + 1, char2_id):
        _char = chr(char_id)
        characters.append(_char)

    return " ".join(characters)


print(get_charecters_between(input(), input()))
