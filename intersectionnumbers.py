def intersection(nums1, nums2):
    solution_set = []
    nums_1_d = dict()
    nums_2_d = dict()
    for el in nums1:
        if(nums_1_d.get(el, 0) == 0):
            nums_1_d[el] = 1
        else:
            nums_1_d[el] +=1
    
    for el in nums2:
        if(nums_2_d.get(el, 0) == 0):
            nums_2_d[el] = 1
        else:
            nums_2_d[el] +=1
    
    for element in nums_1_d:
        if(nums_2_d.get(element,0)>0):
            solution_set.append(element)
    print(solution_set)
            
#intersection([1,2,3,3], [3,3])
intersection([2,4,6,8], [1,3,5,7])
#[2,4,4,8] , [2,4]
