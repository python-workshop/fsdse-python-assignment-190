def add_digits(num):
    if num is None:
        raise TypeError('num cannot be None')
    if num < 0:
        raise ValueError('num cannot be negative')
    digits = []
    while num != 0:
        digits.append(num % 10)
        num //= 10
    digits_sum = sum(digits)
    if digits_sum >= 10:
        return add_digits(digits_sum)
    else:
        return digits_sum