import os
from collections import Counter


os.system("clear")


def delete_chars(line: str, symbol: str) -> str:
    if not isinstance(line, str):
        print("Некорректный ввод!")
    stripped: list = []  # linter suggestion
    for c in line:
        if c == symbol:
            if stripped:
                stripped.pop()

        else:
            stripped.append(c)

    return "".join(stripped)


print("Delete chars first example:", delete_chars("a#bc#d", "#"))
assert delete_chars("a#bc#d", "#") == "bd"
assert delete_chars("abc#d##c", "#") == "ac"
assert delete_chars("abc##d######", "#") == ""
assert delete_chars("#######", "#") == ""
assert delete_chars("", "#") == ""


def candles(candles_number: int, make_new: int) -> int:
    burned = candles_number
    left = candles_number

    while left >= make_new:
        new = left // make_new
        burned += new
        left = left % make_new + new
    return burned


print("Candles first example:", candles(5, 2))

assert candles(5, 2) == 9
assert candles(1, 2) == 1
assert candles(15, 5) == 18
assert candles(12, 2) == 23
assert candles(6, 4) == 7
assert candles(13, 5) == 16
assert candles(2, 3) == 2


def count_total_letters(line: str) -> str:
    for char in line:
        if not char.isalpha():
            return "not a string of letters"
    junk = "".join(f"{i}{j}" for i, j in Counter(line).items())
    return "".join(f"{char}" for char in junk if char != "1")


def count_inline_letters(line: str) -> str:
    if not line:
        return ""

    result: list = []  # linter suggestion
    cnt = 1
    prev_char = line[0]

    for char in line[1:]:
        if char == prev_char:
            cnt += 1
        else:
            result.append(prev_char)
            if cnt > 1:
                result.append(str(cnt))
            prev_char = char
            cnt = 1

    result.append(prev_char)
    if cnt > 1:
        result.append(str(cnt))
    return "".join(result)


print("Count_inline_letters first example:", count_inline_letters("abeehhhhccced"))
assert count_inline_letters("cccbba") == "c3b2a"
assert count_inline_letters("aaabbceedd") == "a3b2ce2d2"
assert count_inline_letters("aaabbceedd") == "a3b2ce2d2"
assert count_inline_letters("abcde") == "abcde"
assert count_inline_letters("aaabbdefffff") == "a3b2def5"
print("Count_total_letters  example:", count_total_letters("abeehhhhccced"))
assert count_total_letters("cccbba") == "c3b2a"
assert count_total_letters("aaabbceedd") == "a3b2ce2d2"
assert count_total_letters("abcde") == "abcde"
assert count_total_letters("aaabbdefffff") == "a3b2def5"
