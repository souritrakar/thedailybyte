import math
points = [[1,1],[-2,-2],]
k=1
res =dict()
def calc_distance(x, y):
  distance = math.floor(math.sqrt((pow(x,2)) + (pow(y,2))))
  return distance

for i in range(0, len(points)): 
  res[calc_distance(points[i][0], points[i][1])] = points[i]

print(res[k])

"""Given a list of points, return the k closest points to the origin (0, 0).

Ex: Given the following points and value of k…

points = [[1,1],[-2,-2]], k = 1, return [[1, 1,]].
"""
