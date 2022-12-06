nums = [1, 2, 3, 4, 4, 5]
isMonotonic = False
mode = 0 #0 if decrease, 1 if increase
smallest = nums[0]

for i in range(0, len(nums)-1):
  if(nums[i] < nums[i+1]):
    mode = 1
    break
  elif nums[i] > nums[i+1]:
    mode = 0
    break

for j in range(0, len(nums)-1):
  if mode == 0:
    #DECREASING
    if nums[j] > nums[j+1]:
      smallest = nums[j+1]

if (mode == 0 and smallest==nums[len(nums)-1]) or (mode == 1 and smallest == nums[0]):
  print(True)
else:
  print(False)

"""
Works with all test cases provided.
This question is asked by Facebook. Given an array nums, return whether or not its values are monotonically increasing or monotonically decreasing.
Note: An array is monotonically increasing if for all values i <= j, nums[i] <= nums[j]. Similarly an array is monotonically decreasing if for all values i <= j, nums[i] >= nums[j].

Ex: Given the following array nums…

nums = [1, 2, 3, 4, 4, 5], return true.

nums = [7, 6, 3], return true.

nums = [8, 4, 6], return false.
"""
