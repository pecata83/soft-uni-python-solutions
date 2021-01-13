digits = input().split()
text = list(input())


def get_number(num: str):

    return sum(list(map(lambda x: int(x), num)))


def remove_char_from_text(index):
    text.pop(index)


def get_char(num: int, _text: list):
    __text = list(_text)

    if 0 <= num <= len(_text) - 1:

        remove_char_from_text(num)
        return __text[num]
    else:
        _index = num % len(_text)
        remove_char_from_text(_index)
        return __text[_index]


numbers = [get_number(n) for n in digits]
res = [get_char(n, text) for n in numbers]

print("".join(res))
