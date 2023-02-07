matrix = [
    [1, 2, 3],
     [4, 5, 6],
     [7,8,9]
]

rows = len(matrix)
columns = len(matrix[0])

res = []

for i in range(columns):
    temp = []
    for j in range(rows):
        temp.append(matrix[j][i])
    res.append(temp)
    
print(res)
        
