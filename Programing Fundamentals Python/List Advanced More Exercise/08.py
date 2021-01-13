targets = [int(t) for t in input().split(" ")]


def shoot_target(_targets: list, _index: int, _power: int):
    __targets = list(_targets)

    if 0 <= _index <= len(__targets):
        __targets[_index] -= _power
    else:
        return __targets

    if __targets[_index] <= 0:
        __targets.pop(_index)

    return __targets


def add_target(_targets: list, _index: int, _value: int):
    __targets = list(_targets)

    if 0 <= _index <= len(__targets) - 1:
        __targets.insert(_index, _value)
    else:
        print("Invalid placement!")

    return __targets


def strike_target(_targets: list, _index: int, _range: int):

    start_index = _index - _range
    end_index = _index + _range

    if start_index >= 0 and end_index <= len(_targets) - 1:

        return [t for i, t in enumerate(
            _targets) if i < start_index or i > end_index]

    else:
        print("Strike missed!")

    return _targets


while True:
    tokens = input().split()
    command = tokens[0]

    if command == "End":
        break

    index = int(tokens[1])
    value = int(tokens[2])

    if command == "Shoot":
        targets = shoot_target(targets, index, value)

    elif command == "Add":
        targets = add_target(targets, index, value)

    elif command == "Strike":
        targets = strike_target(targets, index, value)

targets_strings = [str(t) for t in targets]

print("|".join(targets_strings))
