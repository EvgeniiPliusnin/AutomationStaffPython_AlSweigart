import sys

birthdays = {'Alisa': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Marth 12', }

while True:
    name = input('Type name or <Enter> for exit ')
    if name:
        if name in birthdays:
            print(name + ": birthdays - " + birthdays[name])
        else:
            birthdays[name] = input("I don't now birthday of " + name + ". When is the birthday ?")
            print("updated information about birthdays")
    else:
        sys.exit(-1)

