users = {
    "mohanty@gmail.com": "pass23",
    "sk@gmail.com": "pass1234"
    }

email = input("enter your email")
password = input("enter your password ")


if email in users and users[email] == password:
    print("welcome ")

else:
    print("error ")