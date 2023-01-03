nums = [7, 2, 2, 3, 3, 4, 4]
nums_d = dict()
res = []
for num in nums:
  if(nums_d.get(num, 0) == 0):
    nums_d[num] = 1
  else:
    nums_d[num] +=1

for i in nums_d:
  if nums_d[i] == 2:
    res.append(i)
print(res)

"""
Given an array of integers, nums, each element in the array either appears once or twice. Return a list containing all the numbers that appear twice.
Note: Each element in nums is between one and nums.length (inclusive).

Ex: Given the following array nums…

nums = [2, 3, 1, 5, 5], return [5].
Ex: Given the following array nums…

nums = [1, 2, 3], return [].
Ex: Given the following array nums…

nums = [7, 2, 2, 3, 3, 4, 4], return [2,3,4].
"""
