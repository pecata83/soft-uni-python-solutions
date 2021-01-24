queue = []

while True:
    command = input()

    if command == "End":
        print(f"{len(queue)} people remaining.")
        break
    elif command == "Paid":
        # print("\n".join(queue))
        # queue.clear()
        while len(queue) > 0:
            print(queue.pop(0))
    else:
        queue.append(command)
