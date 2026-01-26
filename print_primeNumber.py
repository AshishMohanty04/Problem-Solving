n = int(input("enter an number "))
number_prime = True 

for i in range(1,n):
    if i % 2 ==0:
        number_prime = False 
        break 


if number_prime :
    print(f"the numbers are : {i}")
