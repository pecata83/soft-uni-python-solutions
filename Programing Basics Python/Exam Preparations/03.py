import math

number = input()
prime_number_sum = 0
nonprime_number_sum = 0


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


while number != "stop":
    num = int(number)

    if num < 0:
        print("Number is negative.")
    elif is_prime(num):
        prime_number_sum += num
    else:
        nonprime_number_sum += num

    number = input()

else:
    print(f"Sum of all prime numbers is: {prime_number_sum}")
    print(f"Sum of all non prime numbers is: {nonprime_number_sum}")
