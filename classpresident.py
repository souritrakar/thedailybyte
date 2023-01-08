votes = [1, 3, 2, 3, 1, 2, 3, 3, 3]
votes_d = dict()
for vote in votes:
  if(votes_d.get(vote, 0) == 0):
    votes_d[vote] = 1
  else:
    votes_d[vote] +=1

def find_max_value(dictionary):
    max_value = float('-inf')
    winner = ""
    output = []
    for key, value in dictionary.items():
        if value > max_value:
            max_value = value
            winner = key
    output.append(winner)
    output.append(max_value)
    return output

print(find_max_value(votes_d)[0])

"""
Each presidential candidates is represented by a unique integer and the candidate that should win the election is the candidate that has received more than half the votes. Given a list of integers, return the candidate that should become the class president.
Note: You may assume there is always a candidate that has received more than half the votes.

Ex: Given the following votes…
votes = [1, 1, 2, 2, 1], return 1.
Ex: Given the following votes…
votes = [1, 3, 2, 3, 1, 2, 3, 3, 3], return 3.
"""
