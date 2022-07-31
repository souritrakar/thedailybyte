def uncommon(sen1, sen2):
    solution_set = []
    sen1d = dict()
    sen2d = dict()
    for word in sen1.split(" "):
        if(sen1d.get(word, 0) == 0):
            sen1d[word] = 1
        else:
            sen1d[word] +=1
    
    for word in sen2.split(" "):
        if(sen2d.get(word, 0) == 0):
            sen2d[word] = 1
        else:
            sen2d[word] +=1
    
    for word in sen1d:
        if(sen2d.get(word,0) == 0):
            solution_set.append(word)
    
    for word in sen2d:
        if(sen1d.get(word,0)== 0):
            solution_set.append(word)
            
    print(solution_set)
 
sen1 = input("Enter sentence 1")
sen2 = input("Enter sentence 2")
uncommon(sen1, sen2)
