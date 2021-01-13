words_str = input()
searched_palindrome = input()

words = words_str.split()

palindromes = [word for word in words if word == word[::-1]]

print(palindromes)
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")
