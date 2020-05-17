from random import randint


def cointoss():
    flip = int(input("Enter the amount of times that you'd like for coin to be tossed: "))
    return flip


def tosschecker(toincoss = 0, heads = 0, tails = 0, streak = 6):
    current_streak_heads = 0
    total_streak_heads = 0
    current_streak_tails = 0
    total_streak_tails = 0


    for i in range(toincoss):
        result = randint(0,1)
        if result == 0:
            heads += 1
            current_streak_heads += 1
            if current_streak_heads >= streak:
                total_streak_heads += 1
        elif result == 1:
            tails += 1
            current_streak_tails += 1
            if current_streak_tails >= streak:
                total_streak_tails += 1


    headspercentage = heads/toincoss * 100
    tailspercentage = tails/toincoss * 100
    return heads, tails, total_streak_heads, total_streak_tails, headspercentage, tailspercentage


def run():
    start = True
    yourtoss = cointoss()
    while start:
        onlyhead, onlytail, total_streak_heads,total_streak_tails, headspercentage, tailspercentage = tosschecker(yourtoss)
        print(f"Total amount of heads is: {onlyhead}")
        print(f"Total amount of tails is: {onlytail}")
        print(f"Total amount of heads-streak is: {total_streak_heads}")
        print(f"Total amount of tails-streak is: {total_streak_tails}")
        # print(f'percentages: heads = {heads/tosses*100}%, tails = {tails/tosses*100}%')
        print(f"percentages: heads = {headspercentage}%, tails = {tailspercentage}%")
        break


run()




