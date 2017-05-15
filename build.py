def build(num):
    if num is None:
        return False
    if num < 0:
        return False
    if num == 0:
        return 0
    elif num % 9 == 0:
        return 9
    else:
        value = num % 9
        return  True