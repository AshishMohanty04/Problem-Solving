def find_largest(arr):
    if len(arr) == 0:
        return None

    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    return largest


# Example
print(find_largest([3, 7, 2, 9, 4]))
