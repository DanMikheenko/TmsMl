def calcucate(variable: float) -> float:
    import math

    first = math.cos(math.exp(variable))
    second = math.log(1 + variable) ** 2
    thind = math.sqrt(math.exp(math.cos(variable)) + (math.sin(math.pi * variable) ** 2))
    fourth = math.sqrt(1/variable)
    fifth = math.cos(variable**2)

    result = (first + second + thind + fourth + fifth) ** math.sin(variable)

    return result

print(calcucate(1.79))