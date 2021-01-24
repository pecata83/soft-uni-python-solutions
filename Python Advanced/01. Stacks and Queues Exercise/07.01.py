from collections import deque
from time import strftime
from time import gmtime

robots_list = list(map(lambda x: x.split("-"), input().split(";")))
robots = [[x[0], int(x[1]), 0] for x in robots_list]
products = deque()


def get_time_in_seconds(time):
    time_list = time.split(":")
    return int(time_list[0]) * 3600 + int(time_list[1]) * 60 + int(time_list[2])


starting_time = get_time_in_seconds(input())

while True:
    command = input()
    if command == "End":
        break
    else:
        product = command
        products.append(product)

while products:
    starting_time += 1
    product = products.popleft()

    is_processed = False

    for robot in robots:
        available_from = robot[2]
        time_needed_to_process = robot[1]

        if available_from <= starting_time:
            robot[2] = starting_time + time_needed_to_process
            converted_starting_time = strftime(
                "%H:%M:%S", gmtime(starting_time))
            print(f"{robot[0]} - {product} [{converted_starting_time}]")
            is_processed = True
            break

    if not is_processed:
        products.append(product)


# print(robots)
