nums = [1, 2, 3, 4]

for i in range(0, len(nums)-1):
  print(i,nums[i], nums[i+1])
  if i%2==0 and nums[i]%2!=0 and nums[i+1]%2==0:
    temp = nums[i+1]
    nums[i+1] = nums[i]
    nums[i] = temp

print(nums)
    
"""
This question is asked by Amazon. Given an array of integers, nums, sort the array in any manner such that when i is even, nums[i] is even and when i is odd, nums[i] is odd.
Note: It is guaranteed that a valid sorting of nums exists.

Ex: Given the following array nums…

nums = [1, 2, 3, 4], one possible way to sort the array is [2,1,4,3]
"""
