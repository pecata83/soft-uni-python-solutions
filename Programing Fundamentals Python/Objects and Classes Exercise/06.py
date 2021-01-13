text = input()
# text = "aaaaabbbbbcdddeeeedssaa"

converted_text = ""

for i, c in enumerate(text):
    if len(converted_text) < 1 or converted_text[-1] != c:
        converted_text += c

print(converted_text)
