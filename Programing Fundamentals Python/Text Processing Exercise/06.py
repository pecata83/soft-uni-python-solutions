# text = input()
text = "aaaaabbbbbcdddeeeedssaa"

result = ""

for i, c in enumerate(text):
    if len(result) == 0 or result[-1] != c:
        result += c

print(result)
