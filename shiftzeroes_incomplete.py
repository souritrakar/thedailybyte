nums = [0, 4, 0, 5, 0, 2 ,1, 8, 0, 4]

for i in range(0, len(nums)-1):
    #
    if i!=len(nums)-1:
        if nums[i]==0 and nums[i+1]!=0:
            temp = nums[i+1]
            nums[i+1] = nums[i]
            nums[i] = temp

for j in range(len(nums)-1,0,-1):
    print(j)
    if (j!=0) and (j!=len(nums)-1):
        if nums[j]==0 and nums[j+1]!=0:
            temp = nums[j+1]
            nums[j+1] = nums[j]
            nums[j] = temp

print(nums)
    
