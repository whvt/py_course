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


print("Sequense func ans:", sequence([1, 2, 3]))
print("Sequense func ans:", sequence([1, 2, 3]))
print("Sequense func ans:", sequence([1, 3, 2]))
print("Sequense func ans:", sequence([1, 2, 1, 2]))
print("Sequense func ans:", sequence([1, 3, 2, 1]))
print("Sequense func ans:", sequence([1, 2, 3, 4, 5, 3, 5, 6]))
print("Sequense func ans:", sequence([40, 50, 60, 10, 20, 30]))
print("Sequense func ans:", sequence([40, 50, 60, 80, 10, 90]))
##############
print("is_opposite func ans: ", is_opposite(10, 6))
print("is_opposite func ans: ", is_opposite(11, 6))
print("is_opposite func ans: ", is_opposite(10, 4))
print("is_opposite func ans: ", is_opposite(10, 2))
print("is_opposite func ans: ", is_opposite(12, 2))
##############
print("is_valid func ans: ", is_valid(123))
print("is_valid func ans: ", is_valid(4561261212345464))
print("is_valid func ans: ", is_valid(4561261212345467))
print("is_valid func ans: ", is_valid(378282246310005))
print("is_valid func ans: ", is_valid(""))
print("is_valid func ans: ", is_valid(56105911231018250))
print("is_valid func ans: ", is_valid(6011000990139424))
print("is_valid func ans: ", is_valid(5105105105105100))
