numbers = input().split(", ")
# numbers = "123, 323, 421, 121".split(", ")


def is_palindrome(num: str):
    reversed_num = num[::-1]

    if reversed_num == num:
        return True
    else:
        return False


for num in numbers:

    if is_palindrome(num):
        print("True")
    else:
        print("False")
