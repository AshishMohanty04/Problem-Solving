arr = [34, 45, 12, 1, 89, 90, 34, 13, 68937464]

smallest = arr[0]

for i in arr:
    if i < smallest:
        smallest = i
print(f"the smallest element is {smallest}")