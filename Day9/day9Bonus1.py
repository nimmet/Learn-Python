
password = input("Enter a new password: ")

result = {}
upper = False
digit = False
length = False

for i in password:
    if i.isupper():
        upper = True

    if i.isdigit():
        digit =True


if len(password) >= 8:
    length = True

result["Digit"] = digit
result["Upper"] = upper
result["Length"] = length


if all(result.values()):
    print("Strong password!")
else:
    print("Weak password!")

