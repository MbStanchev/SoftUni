temp = float(input())
if 5.00 <= temp <= 11.90:
    print("Cold")
elif 12.00 <= temp <= 14.90:
    print("Cool")
elif 15.00 <= temp <= 20.00:
    print("Mild")
elif 20.10 <= temp <= 25.90:
    print("Warm")
elif 26.00 <= temp <= 35.00:
    print("Hot")
else:
    print("unknown")