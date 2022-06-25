import random
range_min = 1
range_max = 20
secretNumber = random.randint(range_min, range_max)
print('я загадал число от ' + str(range_min) + ' до ' + str(range_max))
attempt_count = 0
response = 0
attempt_max = 6
while response != secretNumber:
    print('отгадайте число')
    response = int(input())
    attempt_count += 1
    if response > secretNumber:
        print('Я загадал меньшее число')
    elif response < secretNumber:
        print('Я загадал большее число')
    elif response == secretNumber:
        print('Отлично! Количество попыток: ' + str(attempt_count))
        break
    if attempt_count == attempt_max:
        print('Вам не повезло. Я загадал число ' + str(secretNumber))
        break

