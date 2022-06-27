import random

heads = [1, 1, 1, 1, 1, 1]
tails = [0, 0, 0, 0, 0, 0]
numberOfStreaks = 0
streaks = 100000

for experimentNumber in range(streaks):
    # code create list with 100 coins
    coins = []
    for i in range(0, 100):
        coins.append(random.randint(0, 1))
    # code check sequence of 6 same coins
    for i in range(0, 100 - 5):
        if (coins[i:i + 6] == heads) or (coins[i:i + 6] == tails):
            numberOfStreaks += 1

print('the probability of series is: %s%%' % (numberOfStreaks / streaks / 100))
