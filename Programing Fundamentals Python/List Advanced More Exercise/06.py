numbers_input = input()
numbers = [int(n) for n in numbers_input.split(", ")]
start_group = 10


def remove_from_group(nums: list, nums_to_remove: list):

    for n in nums_to_remove:
        nums.remove(n)

    return nums


while True:
    if len(numbers) <= 0:
        break

    current_group = list(filter((lambda x: x <= start_group), numbers))
    numbers = remove_from_group(numbers, current_group)

    print(f"Group of {start_group}'s: {current_group}")

    start_group += 10
