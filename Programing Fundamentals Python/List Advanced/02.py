todos = []

while True:
    command = input()

    if command == "End":
        break

    tokens = command.split("-", maxsplit=1)

    importance = int(tokens[0])
    todo = tokens[1]

    todos.append((importance, todo))


def sort_fn(task):
    return task[0]


result = [todo for importance, todo in sorted(todos, key=sort_fn)]

print(result)
