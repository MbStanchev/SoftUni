f = float(input())
is_in = True
while is_in:
    if 1 <= f <= 100:
        is_in = False
        break
    f = float(input())
if not is_in:
    print(f"The number {f} is between 1 and 100")
