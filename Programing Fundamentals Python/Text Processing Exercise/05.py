text = input().split()

for word in text:
    if word[0] == ":":
        w = word

        if w[-1] == "." or w[-1] == ",":
            w = word[:-1]

        if 1 < len(w) < 3:
            _w = w[0] + w[1]
            print(_w)
