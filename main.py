import os

os.system("clear")


def hwTime(n):
    if isinstance(n, int) and n >= 0:
        hours = (n // 60) % 24
        rem_minutes = n % 60

        time_str = f"{hours:02d}:{rem_minutes:02d}"

        time_sum = sum(int(char) for char in time_str if char.isdigit())

        print(f"Вы ввели: n = {n}, ответ : {time_sum}")
    else:
        print("Проверь ввод!")


def hwLevelUp(exp, threshold, reward):
    inpt = f"Вы ввели: exp = {exp}, threshold = {threshold}, reward = {reward}, "

    res = True

    if isinstance(exp, int) and isinstance(threshold, int) and isinstance(reward, int):
        total_exp = exp + reward
        if total_exp >= threshold:
            res = True
            print(inpt, f"ответ: {res}")
        else:
            res = False
            print(inpt, f"ответ: {res}")
    else:
        print("Проверь ввод!")


def hwTimeConverter(time24):
    if isinstance(time24, str) and len(time24) == 5:
        hours, minutes = int(time24.split(":")[0]), int(time24.split(":")[1])
        am_pm = "a.m." if hours < 12 else "p.m."
        hours = hours % 12
        if hours == 0:
            hours = 12
        time12 = f"{hours}:{minutes:02d} {am_pm}"
        print(f"Вы ввели - {time24}, ответ: {time12}")
    else:
        print("Проверь ввод!")


if __name__ == "__main__":
    hwTime(808)
    hwLevelUp(10, 15, 5)
    hwTimeConverter("23:12")
