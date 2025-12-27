def twoSum(nums , target):
    for i in range(0,len(nums)):
        for j in range(1,len(nums)-1):
            if nums[i] + nums[j]  == target:
                return [i,j]
nums=[3, 9, 5, 7]
target = 14
print(twoSum(nums , target))

