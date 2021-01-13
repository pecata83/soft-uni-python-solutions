def get_loading_bar(num):
    loading_bar = ["%", "%", "%", "%", "%", "%", "%", "%", "%", "%"]

    if 0 <= percentage < 100:
        steps = int(percentage / 10)

        for s in range(9, 0, -1):
            if s >= steps:
                loading_bar[s] = "."

        return f'{num}% [{"".join(loading_bar)}]\nStill loading...'

    elif percentage == 100:
        return f'100% Complete! \n[{"".join(loading_bar)}]'


percentage = int(input())
result = get_loading_bar(percentage)

print(result)
