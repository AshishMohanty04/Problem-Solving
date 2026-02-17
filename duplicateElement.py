arr = [1, 2, 2, 3, 4, 4, 5]

unique = []

for i in range(len(arr)):
    duplicate = False
    
    for j in range(i):
        if arr[i] == arr[j]:
            duplicate = True
            break
    
    if not duplicate:
        unique.append(arr[i])

print(unique)
