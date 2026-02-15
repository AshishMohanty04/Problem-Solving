n = int(input("enter an number: "))
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True
        
if is_prime(n):
    print("the number is prime")
else:
    print("the number is not prime ")
