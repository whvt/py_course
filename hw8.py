import os
import random

os.system("clear")


def BullsCows(number, attempt):
    bulls = 0
    cows = 0
    number = str(number)
    for i in range(4):  # range(len(attempt))
        if number[i] == attempt[i]:
            bulls += 1
        elif number[i] in attempt:
            cows += 1

    if cows != bulls:
        cows -= bulls
    return bulls, cows


def hwPyramid(symbol, rows):
    if isinstance(rows, int) and rows >= 0 and isinstance(symbol, str):
        for row in range(rows):
            symbols = symbol * (2 * row + 1)
            print(symbols.center(2 * rows - 1))
    else:
        print("Проверь ввод!")


def hwStatues(sizes):
    # if not isinstance(sizes, list):
    #     print("Проверь ввод!")
    # else:
    #     cntr = 0
    #     sizes.sort()
    #     for i in range(len(sizes) - 1):
    #         delta = sizes[i + 1] - sizes[i]
    #         if delta > 1:
    #             cntr += delta - 1

    #     print(f"Для задачи со статуэтками ответ: {cntr}")
    sizes.sort()
    statues = []
    for size in range(sizes[0], sizes[-1] + 1):
        if size not in sizes:
            statues.append(size)
    print(f"Статуи: {statues}, кол-во: {len(statues)}")


def hwGame():
    cntr = 0

    digits = random.sample("1234567890", 4)

    number = int("".join(digits))
    if number < 1000:
        number *= 10
    print("чшшш", "-", number)
    print("Угадай число!")
    while True:
        attempt = input("Давай попытку ->")
        if len(attempt) != 4 or not attempt.isdigit() or len(set(attempt)) != 4:
            print("Не балуйся, проверь ввод")
            continue
        cntr += 1
        bulls, cows = BullsCows(number, attempt)
        print(f"быки: {bulls} коровы: {cows}")

        if bulls == 4:
            print(f"Поздравляю, угадал за {cntr} попыток")
            break


if __name__ == "__main__":
    hwPyramid("'", 10)
    hwStatues([3, 2, 8, 4, 5])
    hwGame()
