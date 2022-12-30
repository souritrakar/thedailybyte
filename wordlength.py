s = "The Daily Byte"
counter = 0
for i in range(len(s)-1, -1, -1):
  if s[i]== " ":
    break
  else:
    counter+=1
print(counter)

"""
Given a string, s, return the length of the last word.
## Note: You may not use any sort of split() method.

Ex: Given the following string…

s = "The Daily Byte", return 4 (because "Byte" is four characters long).
"""
