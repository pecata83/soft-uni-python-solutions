word = list(input())

capitals_index_list = [i for i in range(len(word)) if word[i].isupper()]

print(capitals_index_list)
