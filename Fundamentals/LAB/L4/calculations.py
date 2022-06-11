operator = input()
f_num = int(input())
s_num = int(input())

def calculations(op, f, s):
    result = None
    if operator == "multiply":
        result = f * s
    elif operator == "divide":
        result = f // s
    elif operator == "add":
        result = f + s
    elif operator == "subtract":
        result = f - s
    return result
print(calculations(operator, f_num, s_num))