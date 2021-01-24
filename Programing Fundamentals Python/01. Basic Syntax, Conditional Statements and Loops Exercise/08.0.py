word1 = input()
word2 = input()

passed_words = []

for i in range(0, len(word1)):
    new_word = ""

    for _i in range(0, i + 1):
        new_word += word2[_i]

    for _i in range(i+1, len(word1)):
        new_word += word1[_i]

    if new_word == word1:
        continue

    if new_word not in passed_words:
        print(new_word)

    passed_words.append(new_word)
