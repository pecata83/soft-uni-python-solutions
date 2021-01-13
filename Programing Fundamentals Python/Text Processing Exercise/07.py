text = input()
# text = "pesho>2sis>1a>2akarate>4hexmaster"
text_list = list(text).copy()

explosion_strength = 0


def explode(from_index, strength):
    strength = strength

    for i in range(from_index, from_index + strength):
        if i < len(text_list) and text_list[i] != ">":
            text_list[i] = "@"
            strength -= 1
        else:
            break

    return strength


for i, c in enumerate(text):
    if c == ">":
        strength = explosion_strength + int(text[i+1])
        remaining_strength = explode(i+1, strength)
        explosion_strength = remaining_strength

print("".join(text_list).replace("@", ""))
