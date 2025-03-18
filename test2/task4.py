def add_one(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    return [1] + digits


print(add_one([9]))
print(add_one([1, 2, 3]))
print(add_one([1, 1, 9]))
print(add_one([9, 9, 9]))
