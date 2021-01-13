ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"

num_n = int(input())
num_l = int(input())


for n in range(1, num_n+1):
    for n1 in range(1, num_n + 1):
        for l in range(0, num_l):
            letter1 = ascii_lowercase[l]
            for l1 in range(0, num_l):
                letter2 = ascii_lowercase[l1]
                for n2 in range(1, num_n+1):
                    number_string = str(n) + str(n1) + \
                        letter1 + letter2 + str(n2)
                    if n2 > n and n2 > n1:
                        print(number_string, end=' ')
