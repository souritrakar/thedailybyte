word = input("Enter word")
unique = ""
word_d = dict()

for char in word:
        if(word_d.get(char, 0) == 0):
            word_d[char] = 1
        else:
            word_d[char] +=1
            
for character in word_d:
    if(word_d.get(character,0) == 1):
        unique += character

print(word.index(unique[0]) if len(unique)>1 else word.index(unique))
