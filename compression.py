chars = ['a', 'a', 'b', 'b', 'c', 'c']
chars_d = dict()
result = []

for char in chars:
        if(chars_d.get(char, 0) == 0):
            chars_d[char] = 1
        else:
            chars_d[char] +=1
            
for el in chars_d:
    result.append(el)
    if(chars_d[el] != 1):
        result.append(chars_d[el])
    
print(result)
print("Length is "+ str(len(result)))

"""
This question is asked by Facebook. Given a character array, compress it in place and return the new length of the array.
Note: You should only compress the array if its compressed form will be at least as short as the length of its original form.

Ex: Given the following character array chars…

chars = ['a', 'a', 'a', 'a', 'a', 'a'], return 2.
chars should be compressed to look like the following:
chars = ['a', '6']
Ex: Given the following character array chars…

chars = ['a', 'a', 'b', 'b', 'c', 'c'], return 6.
chars should be compressed to look like the following:
chars = ['a', '2', 'b', '2', 'c', '2']
Ex: Given the following character array chars…

chars = ['a', 'b', 'c'], return 3.
In this case we chose not to compress chars.
"""
