word = input()

vowels = {
    "a": 1,
    "e": 2,
    "i": 3,
    "o": 4,
    "u": 5
}

vowels_sum = 0

for letter in word:
    if letter in vowels:
        vowels_sum += vowels[letter]

print(vowels_sum)
