n = int(input())
result = []
matrix = []
for i in range(n):
    row = [(int(x)) for x in input().split(', ')]
    matrix.append(row)
result = [num for row in matrix for num in row]
# for j in range(n):
#     for nums in matrix[j]:
#         result.append(nums)
print(result)