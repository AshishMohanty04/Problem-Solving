# arr = [23, 45, 12, 56, 11, 10]
# arr.sort()
# print(arr)
# print(f"the second largest element is {arr[-2]}")


def find_second_largest(arr):

    # If array has less than 2 elements
    if len(arr) < 2:
        return None

    # Step 1: Find largest
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    # Step 2: Find second largest
    second = None

    for num in arr:
        if num != largest:   # Ignore largest number

            if second is None:
                second = num

            elif num > second:
                second = num

    return second


# Example
print(find_second_largest([3, 7, 2, 9, 4]))

