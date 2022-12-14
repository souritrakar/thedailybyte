nums = [6, 3, 1, 2, 0, 5]
nums = sorted(nums)
number = 0

for i in range(0, len(nums)-1):
  if(nums[i+1] - nums[i] != 1):
    number = nums[i]+1

print(number)

"""
This question is asked by Amazon. Given an array that contains all distinct values from zero through N except one number, return the number that is missing from the array.

Ex: Given the following array nums…

nums = [1, 4, 2, 0], return 3.
3 is the only number missing in the array between 0 and 4.
Ex: Given the following array nums…

nums = [6, 3, 1, 2, 0, 5], return 4.
4 is the only number missing in the array between 0 and 6.
"""
