def operate(operator, *args):
    first_el = args[0]
    if operator == "+":
        result = 0
        for el in args:
            result += el
        return result
    if operator == "-":
        result = 0
        for el in args[1::]:
            result = first_el - el
            first_el = result
        return result
    if operator == "*":
        result = 1
        for el in args:
            result *= el
        return result
    if operator == "/":
        result = 0
        for el in args[1::]:
            result = first_el / el
            first_el = result
        return result


print(operate("/", 0, 2, 5))
