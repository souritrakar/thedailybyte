original = "byte"
vowels = ['a', 'e', 'i', 'o', 'u']
final = ""
for letter in original:
    if letter not in vowels:
        final+=letter

print(final)

"""
This question is asked by Amazon. Given a string s remove all the vowels it contains and return the resulting string.
Note: In this problem y is not considered a vowel.

Ex: Given the following string s…

s = "aeiou", return ""
Ex: Given the following string s…

s = "byte", return "byt"

"""
