def collatz(num):
    if num % 2 == 0:             # check even number
        print(str(num // 2))
        return num // 2
    else:                           # check odd number
        print(str(3 * num + 1))
        return 3 * num + 1


def inputKeyBoard():
    try:
        num = int(input())
        return num
    except ValueError:
        print('Enter an integer')
        inputKeyBoard()


print('********************************************')
print('Type number for generate sequence of collatz:')
number = inputKeyBoard()
while number != 1:
    number = collatz(number)
