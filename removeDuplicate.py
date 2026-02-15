n = [2, 4, 1, 6]

duplicate = True
for i in range(0, len(n)-1):
    for j in range(1, len(n)):
        if n[i] == n[j]:
            duplicate =  False 

print(f"duplicate found{duplicate}")