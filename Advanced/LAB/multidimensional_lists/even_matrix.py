n = int(input())
result = []
for i in range(n):
    row = [(int(x)) for x in input().split(', ')]

    result.append([x for x in row if x % 2 == 0])
print(result)

# n = int(input())
# res = []
#
# matrix = [[(int(x)) for x in input().split(', ') if int(x) % 2 == 0] for _ in range(n)]
# # res.append([x for x in matrix[0] if x % 2 ==0])
# # for el in range(n):
# #     for e in matrix[el]:
# #         if e % 2 == 0:
# #             res.append(e)
#
# print(matrix)