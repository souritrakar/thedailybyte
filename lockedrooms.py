#rooms = [[1], [2], []]
rooms = [[1, 2], [2], [0], []]
flag = True

for i in range(0, len(rooms)-1):
  print(rooms[i], rooms[i+1])
  if (i+1 in rooms[i]) == False:
    flag = False
    break

print(flag)

#Note: Works with both test cases provided, along with tried test cases; Not completely sure whether this works on all cases or not. Will fix time complexity (O(n^2)) issue later.
"""
This question is asked by Amazon. Given N distinct rooms that are locked we want to know if you can unlock and visit every room. Each room has a list of keys in it that allows you to unlock and visit other rooms. We start with room 0 being unlocked. Return whether or not we can visit every room.
Ex: Given the following rooms…

rooms = [[1], [2], []], return true
Ex: Given the following rooms…

rooms = [[1, 2], [2], [0], []], return false, we can’t enter room 3.
"""
