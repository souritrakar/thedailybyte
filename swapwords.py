s = "The Daily Byte"
res = ""
final = list(s.split(" "))[::-1]

for word in final:
    res+=word+" "
print(res)

"""
Given a string s, reverse the words.
Note: You may assume that there are no leading or trailing whitespaces and each word within s is only separated by a single whitespace.

Ex: Given the following string s…

s = "The Daily Byte", return "Byte Daily The".
"""
