import sys

y = int(input())

def nextHappyYear(year):
    for n in range(year + 1, sys.maxsize + 1):
        n_string = str(n)
        is_happy_year = True

        for symbol_position in range(len(n_string)):
            symbol = n_string[symbol_position]

            if n_string.count(symbol) > 1:
                is_happy_year = False
                break

        if is_happy_year:
            return n_string

print( nextHappyYear(y) )