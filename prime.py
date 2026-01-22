n = int(input("enter an number : "))
is_prime = True
for i in range (2,n-1):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print("this is primr number ")
else:
    print("this is not an prime number ")
