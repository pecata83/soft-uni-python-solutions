def replace_all(first, second):
    if first in second:
        second = second.replace(first, "", 1)
        return replace_all(first, second)
    else:
        return second


print(replace_all(input(), input()))
