
password = input("Enter a new password: ")
upper=False
digit=False

for i in password:
    if i.isdigit():
        digit=True

    if i.isupper():
        upper=True

if len(password)>8 and digit and upper:
    print("Strong password!")

else:
    print("Weak password!")