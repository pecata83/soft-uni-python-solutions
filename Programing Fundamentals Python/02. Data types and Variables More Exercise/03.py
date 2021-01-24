def is_prime(num):
    if num > 1:
        for i in range(2, num//2):
            if (num % i) == 0:
                return False
            else:
                return True
    else:
        return False


print(is_prime(int(input())))
