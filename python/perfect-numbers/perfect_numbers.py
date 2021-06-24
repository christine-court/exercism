def classify(number):
    if not number > 0:
        raise ValueError("Number must be greater than zero")
    elif number == 1:
        return "deficient"

    import math

    factors = {1}
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors = factors.union([i, number // i])
            print(factors)

    if sum(factors) == number:
        return "perfect"
    elif sum(factors) > number:
        return "abundant"
    elif sum(factors) < number:
        return "deficient"
