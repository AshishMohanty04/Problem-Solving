n = int(input("Enter a number: "))

for num in range(2, n + 1):
    number_prime = True

    for i in range(2, num):
        if num % i == 0:
            number_prime = False
            break

    if number_prime:
        print(num)
