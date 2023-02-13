input_arr = [9,9]
number = 0
res = []
for i in range(len(input_arr)):
    number += input_arr[i] * 10**((len(input_arr)-i)-1)

for char in str(number+1):
    res.append(int(char))
print(res)

"""
Given an array digits that represents a non-negative integer, add one to the number and return the result as an array.

Ex: Given the following digits...

digits = [1, 2], return [1, 3].
Ex: Given the following digits...

digits = [9, 9], return [1, 0, 0].
"""
