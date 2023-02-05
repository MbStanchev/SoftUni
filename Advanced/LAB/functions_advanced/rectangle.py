def rectangle(lenth, widgh):
    def par():
        return f'Rectangle perimeter: {(2 * lenth) + (2 * widgh)}'

    def area():
        return f'Rectangle area: {lenth * widgh}'
    if not isinstance(lenth, int) or not isinstance(widgh, int):
        return "Enter valid values!"

    return area() + "\n" + par()


print(rectangle(2, 10))
