number = int(input("enter an number :" ))
number = str(number)

if number == number[::-1]:
    print("this number is palindrome number ")
else:
    print("this number is not palindrome ")
