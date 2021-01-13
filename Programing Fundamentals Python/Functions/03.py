def repeat_str(str, times):
    repeated_string = ""

    for _ in range(times):
        repeated_string += str

    return repeated_string


string_to_return = input()
times = int(input())

print(repeat_str(string_to_return, times))
