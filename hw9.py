import os


os.system("clear")


def sequence(s):
    cnt = 0
    for i in range(1, len(s)):
        if s[i] <= s[i - 1]:
            cnt += 1
            if cnt > 1:
                return False
            if i > 1 and s[i] <= s[i - 2]:
                s[i] = s[i - 1]
    return cnt <= 1


def is_opposite(n, f_number):
    if n % 2 != 0:
        return "n - нечётное"
    else:
        return (f_number + n // 2) % n


def is_valid(card):
    digits = [int(d) for d in str(card)]
    checksum = 0
    is_second = False
    if (
        not card
        or not str(card).isdigit()
        or len(str(card)) < 13
        or len(str(card)) > 19
    ):
        return "Некорректный ввод"
    for i in range(len(digits) - 1, -1, -1):
        digit = digits[i]
        if is_second:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
        is_second = not is_second
    return checksum % 10 == 0
