import re
#email validation
a = 1
pattern = "[A-Z]+[a-z]+\d+[@!#$%^&*_]+[@][a-z]{5,7}[.][a-z]{2,3}"
def email():
    while a==1:
        txt = input("enter mail id: ")
        x = re.search(pattern,txt)
        if re.search(pattern,txt):
            print("valid email-id")
            print(x.string)
            return True
        else:
            print("invalid email-id")
            return False
y = email()
print(y)
