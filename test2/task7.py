def transform_string(s, n):
    if n <= 0 or n > len(s):
        raise ValueError("Wrong input")

    p = s[:n]
    result = list(p)

    for i in range(n - 2, -1, -1):
        result.append(p[i])

    return "".join(result)


s1 = "123"
print(transform_string(s1, 1))  # "a"
print(transform_string(s1, 2))  # "aba"
print(transform_string(s1, 3))  # "abcba"
print(transform_string(s1, 4))  # "abcdcba"
