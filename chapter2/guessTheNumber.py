# Игра в угадывание чисел
import random

secretNumber = random.randint(1, 20)
print('я загадал число от 1 до 20')

# Игроку даётся 6 попыток
for guessTaken in range(1, 7):
    print('угадайте число')
    guess = int(input())

    if guess < secretNumber:
        print('я загадал большее число')
    elif guess > secretNumber:
        print('я загадал меньшее число')

if guess == secretNumber:
    print('Отлично! Количество попыток: ' + str(guessTaken))
else:
    print('Baм не повезло. Я загадал число ' + str(secretNumber))
