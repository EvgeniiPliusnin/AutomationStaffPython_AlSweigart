catNames = []
while True:
    print('Type name of cat ' + str(len(catNames) + 1) + ' <Enter> for end')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]

print('Names of cats are:')
for name in catNames:
    print(' ' + name)
