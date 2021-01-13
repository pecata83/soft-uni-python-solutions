while True:
    word = input()

    if word == "end":
        break

    print(word, "=", "".join(reversed(word)))
