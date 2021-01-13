# first_list = "arp, live, strong".split(", ")
# second_list = "lively, alive, harp, sharp, armstrong".split(", ")
first_list = input().split(", ")
second_list = input().split(", ")

results = [
    res for res in first_list for _res in second_list if res in _res]

# results = []

# for item in first_list:
#     for second_item in second_list:
#         if item in second_item:
#             results.append(item)
#             break

print(list(dict.fromkeys(results)))
