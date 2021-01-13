number = float(input())
in_curency = input()
out_curency = input()
result = 0

if in_curency == "mm":
    if out_curency == "cm":
        result = number * 0.1
    elif out_curency == "m":
        result = number * 0.001
elif in_curency == "cm":
    if out_curency == "mm":
        result = number * 10
    elif out_curency == "m":
        result = number * 0.01
elif in_curency == "m":
    if out_curency == "mm":
        result = number * 1000
    elif out_curency == "cm":
        result = number * 100
    pass
else:
    print("unknown curency")

print(f'{result:.3f}')
