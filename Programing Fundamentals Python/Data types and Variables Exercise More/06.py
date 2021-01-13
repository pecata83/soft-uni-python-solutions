import sys

number = int(input())

for n in range(number + 1, sys.maxsize + 1):
    n_string = str(n)
    is_happy_year = True

    for symbol_position in range(len(n_string)):
        symbol = n_string[symbol_position]

        if is_happy_year == False: 
            break

        for _symbol_position in range(symbol_position + 1, len(n_string)):
            _symbol = n_string[_symbol_position]
            
            is_happy_year = True

            if symbol == _symbol:
                is_happy_year = False
                break

        # if n_string.count(symbol) > 1:
        #     is_happy_year = False
        #     break

    if is_happy_year:
        print(n_string)
        break