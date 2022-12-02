s = "thedailybyte"
temp_s = s
dictionary = ["the", "daily", "byte"]
counter = 0

for word in dictionary:
    if word in s:
        temp_s = temp_s.replace(word, "")
        if len(temp_s) == (len(s) - len(word)):
            counter+=1
            temp_s = s

if counter == len(dictionary):
    print(True)
else:
    print(False)
    
"""
This question is asked by Amazon. Given a string s and a list of words representing a dictionary, return whether or not the entirety of s can be segmented into dictionary words.
Note: You may assume all characters in s and the dictionary are lowercase.

Ex: Given the following string s and dictionary…

s = "thedailybyte", dictionary = ["the", "daily", "byte"], return true.

Ex: Given the following string s and dictionary…

s = "pizzaplanet", dictionary = ["plane", "pizza"], return false.
"""

#Works for both mentioned test cases.
