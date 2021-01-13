words = input().split()

dictionary = {}

for word in words:
    lowercase_word = word.lower()
    if lowercase_word not in dictionary:
        dictionary[lowercase_word] = 0

    dictionary[lowercase_word] += 1


results = [k for k, v in dictionary.items() if v % 2 == 1]

print(" ".join(results))
