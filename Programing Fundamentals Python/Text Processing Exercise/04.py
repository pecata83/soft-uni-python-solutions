text = input()

encripted_text = ""

for c in text:
    encripted_text += chr(ord(c) + 3)

print(encripted_text)
