from typing import List

def max_subarray_xor(nums: List[int]) -> int:
    n = len(nums)
    max_xor = 0

    for i in range(n):
        for j in range(i, n):
            current = 0
            for k in range(i, j + 1):
                current = current ^ nums[k]
            max_xor = max(max_xor, current)

    return max_xor



nums = [8, 1, 2, 12]
print(max_subarray_xor(nums))
