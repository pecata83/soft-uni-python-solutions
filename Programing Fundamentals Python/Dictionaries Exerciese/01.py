from collections import defaultdict

text_list = defaultdict(int)

text = input()

for char in text:
    if char != " ":
        text_list[char] += 1


for k, v in text_list.items():
    print(k, "->", v)
