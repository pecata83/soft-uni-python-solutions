word1 = input()
word1_list = list(word1)
word2_list = list(input())

passed_words = []

for i, c in enumerate(word2_list):
    word1_list[i] = c

    new_word = "".join(word1_list)

    if new_word != word1 and new_word not in passed_words:
        passed_words.append(new_word)
        print(new_word)
