from collections import defaultdict

num = int(input())
synonyms = defaultdict(list)

for i in range(num):
    word = input()
    synonym = input()

    synonyms[word].append(synonym)

for s, v in synonyms.items():
    print(s, "-", ", ".join(v))
