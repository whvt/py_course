def is_palindrome(s):
    solution = bool(s == s[::-1])

    return solution


print(is_palindrome("mam mam "))
