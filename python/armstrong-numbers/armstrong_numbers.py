def is_armstrong_number(number):
    exp = len(str(number))
    digits = [int(d) ** exp for d in str(number)]

    return number == sum(digits)
