while True:
    print("enter your age")
    age = input()
    if age.isdecimal():
        break
    print("please, enter the number")

while True:
    print("enter new password (only letter and digit)") 
    passwor = input()
    if passwor.isalnum():
        break;
    print("error: only letter an digit")

