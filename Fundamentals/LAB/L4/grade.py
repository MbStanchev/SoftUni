grade = float(input())


def calculate_grade(num):
    result = ""
    if 2.00 <= num <= 2.99:
        result = "Fail"
    elif num <= 3.49:
        result = "Poor"
    elif num <= 4.49:
        result = "Good"
    elif num <= 5.49:
        result = "Very Good"
    elif num <= 6.00:
        result = "Excellent"


    return result


print(calculate_grade(grade))