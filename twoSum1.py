def twoSum(num, target):
    for i in range(len(num)):
        for j in range(i + 1, len(num)):   # avoid same index
            if num[i] + num[j] == target:
                return [i, j]   # return indices

num = [3, 2, 4]
target = 6

print(twoSum(num, target))






