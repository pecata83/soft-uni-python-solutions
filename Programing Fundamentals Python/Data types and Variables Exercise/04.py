lines = int(input())
char_sum = 0

for line in range(0, lines):
    char = input()
    char_sum += ord(char)

print(f"The sum equals: {char_sum}")