def decode_char(char: str, key: int):
    return chr(ord(char) + key)


key = int(input())
chars_number = int(input())
chars = [input() for _ in range(chars_number)]

for char in chars:
    print(decode_char(char, key), end="")
