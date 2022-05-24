num_1 = int(input())
num_2 = int(input())
operato = input()
result = 0
even_odd = ""

if operato == "+" or operato == "-" or operato == "*":
    if operato == "+":
        result = num_1 + num_2
    elif operato == "-":
        result = num_1 - num_2
    else:
        result = num_1 * num_2
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{num_1} {operato} {num_2} = {result} - {even_odd}")

else:
    if num_2 == 0:
        print(f"Cannot divide {num_1} by zero")
    else:
        if operato == "/":
            result = num_1 / num_2
            print(f"{num_1} / {num_2} = {result:.2f}")
        elif operato == "%":
            result = num_1 % num_2
            print(f"{num_1} % {num_2} = {result}")
