myPets = ['Sofi', 'Peter', 'Fat']
print('Type name of pet')
name = input()
if name not in myPets:
    print('I do not have pet with name ' + name)
else:
    print(name + ' is my pet')

