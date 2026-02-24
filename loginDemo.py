# users = {
#     "mohanty@gmail.com": "pass23",
#     "sk@gmail.com": "pass1234"
#     }

# email = input("enter your email")
# password = input("enter your password ")


# if email in users and users[email] == password:
#     print("welcome ")

# else:
#     print("error ")


user = {
    "a@gmail": "12",
    "b@gmail": "123",
    "c@gmail": "1234"
}

email = input("enter your email  :  ")
passw = input("enter your pass  : ")

if email in user:
    if user[email] == passw:
        print("welcome to our home ")
    else:
        print("try again")
else:
    print("no email found ")



# This program is a simple **login system using dictionary**.

# * First, emails and passwords are stored in a dictionary called `users`.
# * Then the program asks the user to enter email and password using `input()`.
# * It checks if the email exists in the dictionary using:

# ```python
# email in users
# ```

# * If email exists, it checks if the password is correct using:

# ```python
# users[email] == password
# ```
# Step 6: Check Password
# if users[email] == password:

# Computer converts:
# users["ashish@gmail.com"]
# Result:
# "1234"
# Now check:
# "1234" == "1234"
# TRUE

# * If both are correct → it prints **Welcome**
# * If password is wrong → it prints **Wrong Password**
# * If email is not found → it prints **Email not found**

# -

