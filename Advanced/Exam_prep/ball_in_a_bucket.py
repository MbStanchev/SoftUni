n = 6
matrix = []
for i in range(n):
    matrix.append(input().split())
suma = 0
for shots in range(3):
    target = input()
    targ = [int(x) for x in target[1:-1].split(', ')]
    if 0 <= targ[0] < len(matrix) and 0 <= targ[1] < len(matrix):
        if matrix[targ[0]][targ[1]] != "B":
            pass
        else:
            matrix[targ[0]][targ[1]] = 0
            for num in range(len(matrix)):
                suma += int(matrix[num][targ[1]])
if suma < 100:
    print(f"Sorry! You need {100 - suma} points more to win a prize.")
elif 100 <= suma < 200:
    print(f"Good job! You scored {suma} points, and you've won Football.")
elif 200 <= suma < 300:
    print(f"Good job! You scored {suma} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {suma} points, and you've won Lego Construction Set.")