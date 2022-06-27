def fooSeparator(listParam):
    length = len(listParam)
    retStr = ''
    if length == 0:
        print('list is empty')
    elif length == 1:
        return str(listParam[0])
    elif length == 2:
        retStr = retStr + str(listParam[0]) + ' and ' + str(listParam[1])
    elif len(listParam) > 2:
        for i in range(0, length - 2):
            retStr = retStr + str(listParam[i]) + ', '
        retStr = retStr + str(listParam[length - 2]) + ' and ' + str(listParam[length - 1])
    return retStr


spam = ['apples', 'bananas', 'tofu', 'cats']
# spam = [1, 'cat']
# spam = ['one', 'two']
print(fooSeparator(spam))
