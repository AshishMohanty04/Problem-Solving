n = int(input("enter an number "))

if n < 1000:
    dis = n * 5/100
    total = n - dis
    print(total)

if 1000 >= n <= 5000:
    dis = n * 10/100
    total = n - dis
    print(total)

if n > 5000:
    dis = n * 15/100
    total = n - dis
    print(total)