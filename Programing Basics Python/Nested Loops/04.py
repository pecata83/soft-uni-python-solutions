start_num = int(input())
end_num = int(input())

magic_num = int(input())

combinations_count = 0
first_combination_number = 0
first_num = 0
second_num = 0
is_combination_found = False

for n1 in range(start_num, end_num + 1):
    if is_combination_found == False:

        for n2 in range(start_num, end_num + 1):
            combinations_count += 1
            if n1 + n2 == magic_num:
                first_num = n1
                second_num = n2
                is_combination_found = True
                break
    else:
        break

if first_num != 0 and second_num != 0:
    print(
        f"Combination N:{combinations_count} ({first_num} + {second_num} = {magic_num})")
else:
    print(f"{combinations_count} combinations - neither equals {magic_num}")
