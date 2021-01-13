tokens = input().split()


def decipher_string(word: str):

    number_list = [n for n in word if n.isnumeric()]
    chars_list = [n for n in word if not n.isnumeric()]

    deciphered_word = list(chars_list)
    deciphered_word[0] = chars_list[-1]
    deciphered_word[-1] = chars_list[0]

    first_char = chr(int("".join(number_list)))

    deciphered_word.insert(0, first_char)

    return "".join(deciphered_word)


deciphered = [decipher_string(w) for w in tokens]

print(" ".join(deciphered))
